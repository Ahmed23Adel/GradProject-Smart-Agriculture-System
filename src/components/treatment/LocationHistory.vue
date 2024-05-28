<script setup>
import { ref, onMounted, watch } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';
import { UserType } from '@/modules/Basic.ts';
import { fetchAllLocations } from '@/modules/CommonRequests.ts';


const locations = ref([])
const selectedLocation = ref();
const isOwner = ref(false);
const images = ref();
const treatmentValue = ref("")
const isShowLoading = ref(true)
const isShowLoadingSaveUpdates = ref(false)
treatmentValue.value = ""

// defineProps(["location"])


const responsiveOptions = ref([
    {
        breakpoint: '1300px',
        numVisible: 4
    },
    {
        breakpoint: '575px',
        numVisible: 1
    }
]);

async function fetchLocationHistory() {
    const requester = new HttpRequester('location-history');
    const today = new Date();
    const dd = String(today.getDate()).padStart(2, '0');
    const mm = String(today.getMonth() + 1).padStart(2, '0'); // January is 0!
    const yyyy = today.getFullYear();
    const formattedDate = `${dd}/${mm}/${yyyy}`;
    const queryParams = {
        location: selectedLocation.value.name,
        from_date: "01/01/0001",
        to_date: formattedDate,
    };
    const requester_data = await requester.callApi('GET', queryParams);
    images.value = requester_data.allHistory;
}



async function updateTreatment(){
    isShowLoadingSaveUpdates.value = true;
    const requester = new HttpRequester('update_treatment');
    const queryParams = {
        location: selectedLocation.value.name,
        treatment: treatmentValue.value,
    };
    await requester.callApi('PUT', queryParams);
    isShowLoadingSaveUpdates.value = false;
}

async function declareLocationTreated(){
    isShowLoadingSaveUpdates.value = true;
    const requester = new HttpRequester('declare_location_healthy');
    const queryParams = {
        location: selectedLocation.value.name,
    };
    await requester.callApi('PUT',queryParams);
    isShowLoadingSaveUpdates.value = false;
}


async function fetchTreatmentValue(){
    const requester = new HttpRequester('get_treatment_value');
    const queryParams = {
        location: selectedLocation.value.name,
    };
    const requester_data  =  await requester.callApi('GET',queryParams);
    treatmentValue.value = requester_data.treatment;
}
function onChangeImage(){
}


watch(selectedLocation, async (newSelectedLocation, oldSelectedLocation) => {
    await fetchLocationHistory();
    await fetchTreatmentValue();
});

onMounted(async () => {
    // TODO selected location is never set here correct it
    isOwner.value = UserType.getInstance().getUserType();
    await fetchAllLocations(locations, selectedLocation);
    selectedLocation.value = locations.value[0];
    isShowLoading.value=false;

});
</script>


<template>
    <div v-if="isShowLoading">
            <ProgressSpinner />
    </div>
    <div class="selectors" v-if="!isShowLoading">
        <el-row>
            <el-col :span="8" :xs="24" :sm="24" :md="24" :lg="8" :xl="8">
                <div class="grid-content ep-bg-purple">
                    <p class="pre-date" style="margin:20px"> Location </p>
                    <div class="card flex justify-content-center" style="margin:20px">
                        <CascadeSelect v-model="selectedLocation" :options="locations" optionLabel="name"
                            optionGroupLabel="name" :optionGroupChildren="['subLocations']" style="min-width: 14rem"
                            placeholder="Select a Location" />
                    </div>
                </div>
            </el-col>
        </el-row>

        <div class="row">
            <div class="col-12">
                <div class="row">
                    <div class="col-6 ">
                        <div class="card images-parent">
                            <Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5"
                                containerStyle="max-width: 640px">
                                <template #item="slotProps">
                                    <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt"
                                        style="width: 100%; display: block" @change="onChangeImage" crossorigin="anonymous" witdth="450px" height="450px"/>
                                </template>
                                <template #thumbnail="slotProps">
                                    <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt"
                                        style="display: block" crossorigin="anonymous"/>
                                </template>
                                <template #caption="slotProps">
                                    <div class="text-xl mb-2 font-bold">{{ slotProps.item.title }}</div>
                                    <p class="text-white">{{ slotProps.item.alt }}</p>
                                </template>
                            </Galleria>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="row">
                            <h1 class="h5"> Treatment (you may edit it to something special)</h1>
                        </div>
                        <div class="row">
                            <div class="card flex justify-content-center text-area-parent">
                                <Textarea v-model="treatmentValue" rows="5" cols="30" />
                            </div>
                        </div>
                        <div class="row">
                            <div class="submit-parent">
                                <div class="card flex justify-content-center submit-sub-parent">
                                    <Button label="Save the updates" icon="pi pi-check" iconPos="right"
                                        class="submit-button" @click="updateTreatment" :disabled="isOwner" />
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="submit-parent">
                                <div class="card flex justify-content-center submit-sub-parent">
                                    <Button label="Declare this location healty" icon="pi pi-check" iconPos="right"
                                        class="submit-button" @click="declareLocationTreated" :disabled="isOwner"/>
                                </div>
                            </div>
                        </div>
                        <div v-if="isShowLoadingSaveUpdates" class="row">
                                <ProgressSpinner />
                        </div>
                        

                    </div>
                </div>

            </div>
        </div>




    </div>



</template>

<style scoped>
.sub-header-gen-stats {
    color: black;
    left: 0%;
}

.selectors {
    /* display: flex;
    flex-direction: row; */
}

.graph-image-parent {
    display: flex;
    justify-content: center;
    /* Center items horizontally */
    align-items: center;
    /* Center items vertically */
}

.pre-date {
    font-size: 28px;
}

.text-area-parent {
    margin-right: 70px;
    border-radius: 20px;
}

.images-parent {
    background-color: var(--primary);
    border: none;
}

.submit-parent {
    display: flex;
    justify-content: center;
    /* Center horizontally */
    align-items: center;
    /* Center vertically */
    margin-top: 30px;
    background-color: var(--primary);
}

.submit-button {
    border-radius: 20px;
}

.submit-sub-parent {
    background-color: var(--primary);
    border: none;
}

.row.align-items-center {
    display: flex;
    align-items: center;
    /* Center vertically */
}

.extend-parent{
    display: flex;
    justify-content: center;
}
</style>