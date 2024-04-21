<script setup>
import { ref, onMounted, watch } from "vue";
import GraphOfImagesTreatment from "./GraphOfImagesTreatment.vue"
import { HttpRequester } from './nets'; // Adjust the file path as necessary
const bearer = 'hi';

const locations = ref([])
const selectedLocation = ref();
const locs = ref()
async function fetchAllLocs() {

    const requester = new HttpRequester('http://127.0.0.1:8000/get-diseased-locations', bearer);
    const requester_data = await requester.callApi();
    locs.value = requester_data.locations;
    console.log(locs.value);
    for (const loc of locs.value) {
        locations.value.push({ name: loc });
    }
    selectedLocation.value = locations.value[0];

}
watch(selectedLocation, async (newSelectedLocation, oldSelectedLocation) => {
    // Call fetchLocationHistory when selectedLocation changes
    await fetchLocationHistory();
});
onMounted(async () => {
    await fetchAllLocs();
    fetchLocationHistory()

});

const images = ref();

async function fetchLocationHistory() {
    const requester = new HttpRequester('http://127.0.0.1:8000/location-history', bearer);
    const queryParams = {
        location: selectedLocation.value,
        from_date: "01/01/0001",
        to_date: "01/01/0001",
    };
    const requester_data = await requester.callApi(queryParams);
    images.value = requester_data.allHistory;
}

onMounted(() => {
    fetchLocationHistory();
});


function update_treatment(){
    const requester = new HttpRequester('http://127.0.0.1:8000/update_treatment', bearer);
    const queryParams = {
        location: selectedLocation.value,
        treatment: treatmentValue.value,
    };
    const requester_data = requester.callApiPut(queryParams);
    console.log("update_treatment")
}


function declare_location_treated(){
    const requester = new HttpRequester('http://127.0.0.1:8000/declare_location_healthy', bearer);
    const queryParams = {
        location: selectedLocation.value,
    };
    const requester_data = requester.callApiPut(queryParams);
    console.log("declare treated")
}

const period_extension = ref()
function extend_location_by_period(){
    const requester = new HttpRequester('http://127.0.0.1:8000/extend_location_by_days', bearer);
    const queryParams = {
        location: selectedLocation.value,
        period: period_extension.value,
    };
    const requester_data = requester.callApiPut(queryParams);
    console.log("extend_location_by_period")
}

// graph of images
defineProps(["location"])
console.log("location Graph", location)

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


const treatmentValue = ref("")
treatmentValue.value = "Cover the soil under the plants with mulch, such as fabric, straw, plastic mulch, or dried leaves. Water at the base of each plant, using drip irrigation, a soaker hose, or careful hand watering. Pruning the bottom leaves can also prevent early blight spores from splashing up from the soil onto leaves."

function onChangeImage(){
    console.log('hi')
}
</script>


<template>

    <div class="selectors">
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
                                        style="width: 100%; display: block" @change="onChangeImage" />
                                </template>
                                <template #thumbnail="slotProps">
                                    <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt"
                                        style="display: block" />
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
                                        class="submit-button" @click="update_treatment" />
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="submit-parent">
                                <div class="card flex justify-content-center submit-sub-parent">
                                    <Button label="Declare this location healty" icon="pi pi-check" iconPos="right"
                                        class="submit-button" @click="declare_location_treated"/>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <h1 class="h5"> Treatment period: 20 days</h1>
                        </div>
                        <div class="row">
                            <h1 class="h5"> Started from: 22-10-2020</h1>
                        </div>
                        <div class="row">
                            <h1 class="h5"> End date at: 12-11-2020</h1>
                        </div>
                        <div class="row align-items-center">
                            <div class="col-3">
                                <h1 class="h5"> Extend by: </h1>

                            </div>
                            <div class="col-3">
                                <div class="flex-auto">
                                    <InputNumber v-model="period_extension" inputId="minmax" :min="0" :max="100" />
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="extend-parent">
                                    <div class="card flex justify-content-center submit-sub-parent">
                                        <Button label="Extend" icon="pi pi-check" iconPos="right"
                                            class="submit-button" @click="extend_location_by_period"/>
                                    </div>
                                </div>
                            </div>
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