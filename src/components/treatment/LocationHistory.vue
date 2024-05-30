<script setup>
import { ref, onMounted, watch } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';
import { UserType } from '@/modules/Basic.ts';
import { fetchAllLocations } from '@/modules/CommonRequests.ts';
import { formatDate } from '@/modules/Basic.ts';


const locations = ref([])
const isLocationNewForExpert = ref([])
const selectedLocation = ref();
const isOwner = ref(false);
const images = ref();
const treatmentValue = ref("")
const isShowLoading = ref(true)
const isShowLoadingSaveUpdates = ref(false)
const isShowErrorMsg = ref(false)
const errorMessage = ref("Error happened while performing this action. Please try again")
treatmentValue.value = ""
const newZonesNames = ref([])
const newZonesNamesConcatenated = ref("")
const isThisLocationChecked = ref(false)
const dates = ref();
const isShowSchedulingDone = ref(false)
const scheduleData = ref()
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
    const formattedDate = `${dd}-${mm}-${yyyy}`;
    const queryParams = {
        location: selectedLocation.value.name,
        from_date: "01-01-1990",
        to_date: formattedDate,
    };
    const requester_data = await requester.callApi('GET', queryParams);
    if (!requester_data) {
        isShowErrorMsg.value = true;
        errorMessage.value = "Error loading images. Please try again"
    }
    images.value = requester_data.allHistory;
}



async function updateTreatment() {
    isShowLoadingSaveUpdates.value = true;
    isShowErrorMsg.value = false;
    const requester = new HttpRequester('update_treatment');
    const queryParams = {
        location: selectedLocation.value.name,
        treatment: treatmentValue.value,
    };
    const requester_data = await requester.callApi('PUT', queryParams);
    if (!requester_data) {
        isShowErrorMsg.value = true;
        errorMessage.value = "Error saving your updates. Please try again"
    }
    isShowLoadingSaveUpdates.value = false;

}

async function declareLocationTreated() {
    isShowLoadingSaveUpdates.value = true;
    isShowErrorMsg.value = false;
    const requester = new HttpRequester('declare_location_healthy');
    const queryParams = {
        location: selectedLocation.value.name,
    };
    const requester_data = await requester.callApi('PUT', queryParams);
    if (!requester_data) {
        isShowErrorMsg.value = true;
        errorMessage.value = "Error declaring your location healthy. Please try again"
    }
    isShowLoadingSaveUpdates.value = false;
}


async function fetchTreatmentValue() {
    const requester = new HttpRequester('get_treatment_value');
    const queryParams = {
        location: selectedLocation.value.name,
    };
    const requester_data = await requester.callApi('GET', queryParams);
    treatmentValue.value = requester_data.treatment;
}
function onChangeImage() {
}


async function sheduleTreatment() {
    console.log("hello")
    console.log(dates.value)
    const requester = new HttpRequester('schedule-zones');
    let start_date_full = dates.value[0]
    let end_date_full = dates.value[1]
    const queryParams = {
        start_date: formatDate(start_date_full),
        end_date: formatDate(end_date_full),
        zone_name: selectedLocation.value.name,
    };
    const requester_data = await requester.callApi('POST', queryParams);
    if (requester_data) {
        isShowSchedulingDone.value = true;
    }
}
function setZoneCheckedByExpert(zoneName) {
    const requester = new HttpRequester('set-location-checked');
    const queryParams = {
        location_name: zoneName,
    };
    requester.callApi('POST', queryParams);

}

async function fetchSceduleData(){
    const requester = new HttpRequester('zone-scheduled');
    const queryParams = {
        location: selectedLocation.value.name,
    };
    // console.log("queryParams", queryParams)
    const requester_data = await requester.callApi('GET', queryParams);
    scheduleData.value = requester_data.schedule;
    console.log("selectedLocation.value", selectedLocation.value)
    console.log("scheduleData.value", scheduleData.value)
}
watch([selectedLocation, isThisLocationChecked], async ([newSelectedLocation, newIsThisLocationChecked], [oldSelectedLocation, oldIsThisLocationChecked]) => {
    // same location but check is diff
    if (oldSelectedLocation && !oldIsThisLocationChecked && newSelectedLocation.name === oldSelectedLocation.name &&
        oldIsThisLocationChecked === false && newIsThisLocationChecked === true) {
        setZoneCheckedByExpert(oldSelectedLocation.name)
        isLocationNewForExpert.value[locations.value.findIndex(location => location.name === selectedLocation.value.name)] = false;
    }
    let selectedLocationIndex = locations.value.findIndex(location => location.name === selectedLocation.value.name);
    isThisLocationChecked.value = !isLocationNewForExpert.value[selectedLocationIndex]
    await fetchLocationHistory();
    await fetchTreatmentValue();
    await fetchSceduleData();
});


onMounted(async () => {
    // TODO selected location is never set here correct it
    isOwner.value = UserType.getInstance().getUserType();
    await fetchAllLocations(locations, selectedLocation, isLocationNewForExpert);
    selectedLocation.value = locations.value[0];
    for (let i = 0; i < locations.value.length; i++) {
        if (isLocationNewForExpert.value[i])
            newZonesNames.value.push(locations.value[i].name)
    }
    const length = newZonesNames.value.length;
    if (length === 0) newZonesNamesConcatenated.value = "";
    else if (length === 1) newZonesNamesConcatenated.value = newZonesNames.value[0];
    else if (length === 2) newZonesNamesConcatenated.value = `${newZonesNames.value[0]} and ${newZonesNames.value[1]}`;
    else newZonesNamesConcatenated.value = `${newZonesNames.value.slice(0, -1).join(', ')}, and ${newZonesNames.value[length - 1]}`;
    isThisLocationChecked.value = !isLocationNewForExpert.value[0]
    // console.log("isThisLocationChecked", isThisLocationChecked.value)
    isShowLoading.value = false;

});


const getSeverity = (product) => {
    console.log("product", product.Done)
    switch (product.Done) {
        case true:
            console.log("true")
            return 'success';
        case false:
            console.log("false")
            return 'danger';

        default:
            return null;
    }
};
</script>


<template>
    <div v-if="isShowLoading">
        <ProgressSpinner />
    </div>
    <div class="selectors" v-if="!isShowLoading">
        <div class="row">
            <div class="col0-12">
                <div class="grid-content ep-bg-purple">
                    <p class="pre-date" style="margin:20px"> Location </p>
                    <div class="card flex justify-content-center" style="margin:20px">
                        <CascadeSelect v-model="selectedLocation" :options="locations" optionLabel="name"
                            optionGroupLabel="name" :optionGroupChildren="['subLocations']" style="min-width: 14rem"
                            placeholder="Select a Location" />
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <Message severity="success">New diseased zones have been added. You should check them: {{
        newZonesNamesConcatenated }}</Message>
        </div>

        <div class="row">
            <div class="col-12">
                <div class="row">
                    <div class="col-6 ">
                        <div class="card images-parent">
                            <Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5"
                                containerStyle="max-width: 640px">
                                <template #item="slotProps">
                                    <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt"
                                        class="fixed-size-image" @change="onChangeImage" crossorigin="anonymous" />
                                </template>
                                <template #thumbnail="slotProps">
                                    <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt"
                                        class="fixed-size-thumbnail" crossorigin="anonymous" />
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
                            <div class="col-6" style="margin-bottom: 20px" v-if="!isThisLocationChecked">
                                <Checkbox v-model="isThisLocationChecked" :binary="true" />
                                Declare this location checked
                            </div>

                        </div>
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
                                        class="submit-button" @click="declareLocationTreated" :disabled="isOwner" />
                                </div>
                            </div>
                        </div>
                        <div class=row>
                            <h3 class="h5" style="margin-top:20px"> Schedule treatment for this location (please select
                                a range)</h3>
                        </div>
                        <div class=row>
                            <div class="col-8">
                                <div class="card flex justify-content-center">
                                    <Calendar v-model="dates" selectionMode="range" :manualInput="false" />
                                </div>
                            </div>
                            <div class="col-4">
                                <button type="button" class="btn btn-primary" @click="sheduleTreatment">Confirm</button>
                            </div>
                        </div>
                        
                        <div class="card row ">
                            <DataTable :value="scheduleData" showGridlines tableStyle="min-width: 50rem"  >
                                <Column field="Date_Scheduled" header="Date"></Column>
                                <Column field="Done" header="Done"></Column>
                                <!-- <Column header="Done">
                                    <template #body="slotProps">
                                        <Tag :value="slotProps.data.Done" :severity="getSeverity(slotProps.data)" />
                                    </template>
                                </Column> -->
                                <Column field="Farmer_Finished" header="Farmer"></Column>
                            </DataTable>
                        </div>

                        <!-- </div> -->
                        <div v-if="isShowLoadingSaveUpdates" class="row">
                            <ProgressSpinner />
                        </div>
                        <div v-if="isShowErrorMsg" class="row" style="margin-top: 10px; margin:10px;">
                            <Message severity="error">{{ errorMessage }}</Message>
                        </div>
                        <div v-if="isShowSchedulingDone" class="row" style="margin-top: 10px; margin:10px;">
                            <Message severity="success">Treatment has been scheduled for this zone</Message>
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

.extend-parent {
    display: flex;
    justify-content: center;
}

.fixed-size-image {
    width: 600px;
    height: 450px;
    object-fit: cover;
    /* or "contain" depending on the desired effect */
    display: block;
}

.fixed-size-thumbnail {
    width: 80px;
    height: 80px;
    object-fit: cover;
    /* or "contain" */
    display: block;
}
</style>