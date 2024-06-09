<script setup>
import { ref, onMounted, watch } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';
import { UserType } from '@/modules/Basic.ts';
import { fetchAllLocations } from '@/modules/CommonRequests.ts';
import { formatDate } from '@/modules/Basic.ts';
import { findCoordinates, openGoogleMapsWithLatLong } from '@/modules/Basic.ts';


const locations = ref([])
const zonesActivePeriodOfDiseas = ref([])
const selectedZonePeriodOfDiseasId = ref("")
const zonesTreatment = ref([])
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
const showSuccessMsg = ref("")
const isShowSuccessMsg = ref(false)

const isShowTableOfTreatments = ref(false)
const allTreatmentNames = ref()
const allTreatmentIds = ref()
const selectedTreatment = ref()
const allTreatmentData = ref()
const isShowSpinnerTreatments = ref(false)
const treatmentName = ref("")

////
const grid = ref([])
const hoveredZone = ref(null)
const calculatedCoordinates = ref({})
const zoneNameSearch = ref("")
const minLat = 40.0;
const maxLat = 40.1;
const minLong = 50.0;
const maxLong = 50.1;
const zoneSize = 500 //m;
const maxZones = 1000;
///
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
        period_of_disease_id: selectedZonePeriodOfDiseasId.value
    };
    const requester_data = await requester.callApi('GET', queryParams);
    if (!requester_data) {
        isShowErrorMsg.value = true;
        errorMessage.value = "Error loading images. Please try again"
    }
    images.value = requester_data.allHistory;
}



async function updateTreatment() {
    isShowTableOfTreatments.value = true;
    isShowSpinnerTreatments.value = true;
    console.log("updateTreatment", updateTreatment)
    updateTreatment.value = true;
    const requester = new HttpRequester('list_saved_treatments');
    const requester_data = await requester.callApi('GET');
    allTreatmentNames.value = requester_data.saved_treatments.map(treatment => ({ name: treatment.treatmentName }));
    allTreatmentIds.value = requester_data.saved_treatments.map(treatment => ({ id: treatment._id }));
    selectedTreatment.value = allTreatmentNames.value[0]
    allTreatmentData.value = requester_data.saved_treatments
    isShowLoading.value = false;
    isShowSpinnerTreatments.value = false;

}

async function endThisPeriodOfDisease() {
    // Display a confirmation dialog using SweetAlert2
    const result = await Swal.fire({
        title: 'Are you sure?',
        text: 'Ending this period of disease is irreversible!',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, end it!'
    });

    if (result.isConfirmed) {
        // Proceed with the action as the user confirmed
        isShowLoadingSaveUpdates.value = true;
        isShowErrorMsg.value = false;
        const requester = new HttpRequester('end_period_of_disease');
        const queryParams = {
            period_of_disease_id: selectedZonePeriodOfDiseasId.value,
            ender_expert_id: UserType.getInstance().getUserId()
        };
        console.log("queryParamsend", queryParams)
        const requester_data = await requester.callApi('PUT', queryParams);
        if (!requester_data) {
            isShowErrorMsg.value = true;
            errorMessage.value = "Error ending this period of disease. Please try again"
        }
        isShowLoadingSaveUpdates.value = false;
        refreshPage(true);
    }
}


function onChangeImage() {
}


async function sheduleTreatment() {
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
    if (!isOwner.value) {
        const requester = new HttpRequester('set-zone-checked');
        const queryParams = {
            period_of_disease_id: selectedZonePeriodOfDiseasId.value,
            expert_id: UserType.getInstance().getUserId()
        };
        console.log("queryParams"), queryParams
        requester.callApi('PUT', queryParams);
    }


}

async function fetchSceduleData() {
    const requester = new HttpRequester('get-treatment-schedule');
    const queryParams = {
        period_of_treatment_id: selectedZonePeriodOfDiseasId.value
    };
    const requester_data = await requester.callApi('GET', queryParams);
    console.log("requester_data", requester_data)
    scheduleData.value = requester_data.schedule;
}

async function saveNewSpecificTreatment() {
    let selectedTreatmentIndex = allTreatmentNames.value.findIndex(treatment => treatment.name === selectedTreatment.value.name);
    let selectedTreatmentId = allTreatmentIds.value[selectedTreatmentIndex].id

    const requester = new HttpRequester('set-period-of-disease-specific-treatment');
    const queryParams = {
        period_of_disease_id: selectedZonePeriodOfDiseasId.value,
        treatment_id: selectedTreatmentId
    };
    console.log("queryParams", queryParams)
    await requester.callApi('PUT', queryParams);
    isShowTableOfTreatments.value = false;
    isShowLoadingSaveUpdates.value = true;

}

function cancelSaveSpecificTreatment(){
    isShowTableOfTreatments.value = false;
    isShowLoadingSaveUpdates.value = false;
}
import Swal from 'sweetalert2';

async function rejectThisPeriodOfDisease() {
    const result = await Swal.fire({
        title: 'Are you sure?',
        text: "This action is irreversible!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, reject it!'
    });
    console.log("result.isConfirmed", result.isConfirmed)
    if (result.isConfirmed) {
        console.log("zonesActivePeriodOfDiseas", zonesActivePeriodOfDiseas)
        console.log("allTreatmentNames", allTreatmentNames)
        let selectedLocationIndex = locations.value.findIndex(location => location.name === selectedLocation.value.name);
        selectedZonePeriodOfDiseasId.value = zonesActivePeriodOfDiseas.value[selectedLocationIndex]
        console.log("selectedZonePeriodOfDiseasId", selectedZonePeriodOfDiseasId)
        const requester = new HttpRequester('reject_period_of_disease');
        const queryParams = {
            period_of_disease_id: selectedZonePeriodOfDiseasId.value,
        };

        // Call the API with the queryParams here
        console.log("rejectqueryParams", queryParams)
        await requester.callApi('DELETE', queryParams)
            .then(response => {
                Swal.fire(
                    'Rejected!',
                    'The period of disease has been rejected.',
                    'success'
                );
                // Handle success response
                console.log('Period of disease rejected successfully', response);
                refreshPage(true)
            })
            .catch(error => {
                Swal.fire(
                    'Error!',
                    'There was an error rejecting the period of disease.',
                    'error'
                );
                // Handle error response
                console.error('Error rejecting period of disease', error);
            });
    } else {
        // If the user did not confirm, do nothing
        console.log('Action canceled by user');
    }
}

async function reseduleTreatmentAgain() {
    const result = await Swal.fire({
        title: 'Reschedule Treatment',
        text: 'Do you want to delete existing items or keep them?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Delete Existing',
        cancelButtonText: 'Keep Existing'
    });

    if (result.isConfirmed) {
        // User chose to delete existing items
        await callRescheduleZoneCheck("delete_existing");
    } else if (result.dismiss === Swal.DismissReason.cancel) {
        // User chose to keep existing items
        await callRescheduleZoneCheck("keep_existing");
    }
    refreshPage(true);
}

async function callRescheduleZoneCheck(reschedule_option) {
    const requester = new HttpRequester('reschedule-zone-check');
    const queryParams = {
        period_of_disease_id: selectedZonePeriodOfDiseasId.value,
        expert_id: UserType.getInstance().getUserId(),
        reschedule_option: reschedule_option
    };
    console.log("queryParams", queryParams);

    try {
        await requester.callApi('PUT', queryParams);
        Swal.fire(
            'Success!',
            'The period of disease has been rescheduled successfully.',
            'success'
        );
        refreshPage(true);
    } catch (error) {
        Swal.fire(
            'Error!',
            'There was an error rescheduling the period of disease.',
            'error'
        );
        console.error('Error rescheduling period of disease', error);
    }
}


watch([selectedLocation, isThisLocationChecked], async ([newSelectedLocation, newIsThisLocationChecked], [oldSelectedLocation, oldIsThisLocationChecked]) => {
    // same location but check is diff
    if (oldSelectedLocation && !oldIsThisLocationChecked && newSelectedLocation.name === oldSelectedLocation.name &&
        oldIsThisLocationChecked === false && newIsThisLocationChecked === true) {
        setZoneCheckedByExpert(oldSelectedLocation.name)
        isLocationNewForExpert.value[locations.value.findIndex(location => location.name === selectedLocation.value.name)] = false;
    }
    let selectedLocationIndex = locations.value.findIndex(location => location.name === selectedLocation.value.name);
    selectedZonePeriodOfDiseasId.value = zonesActivePeriodOfDiseas.value[selectedLocationIndex]
    console.log("selectedZonePeriodOfDiseasId", selectedZonePeriodOfDiseasId)
    isThisLocationChecked.value = !isLocationNewForExpert.value[selectedLocationIndex]
    await fetchLocationHistory();
    treatmentValue.value = zonesTreatment.value[selectedLocationIndex]
    console.log("treatmentValue", treatmentValue)
    await fetchSceduleData();

});

async function refreshPage(isSleep = false) {
    if (isSleep) {
        await new Promise(resolve => setTimeout(resolve, 3000)); // Sleep for 3 seconds
    }
    isOwner.value = UserType.getInstance().getUserType();
    await fetchAllLocations(locations, selectedLocation, isLocationNewForExpert, zonesTreatment, zonesActivePeriodOfDiseas);
    console.log("refresh locations", locations.value)
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
    isShowLoading.value = false;
}
onMounted(async () => {
    // TODO selected location is never set here correct it
    refreshPage()

});


function openGoogleMapsWithLatLongLocal() {
    console.log("selectedLocation", selectedLocation)
    findCoordinates(maxLong, minLong, maxLat, minLat, zoneSize, selectedLocation.value.name, calculatedCoordinates)
    openGoogleMapsWithLatLong(calculatedCoordinates.value)
}
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
                            <div class="col-6" style="margin-bottom: 20px" v-if="!isThisLocationChecked && !isOwner">
                                <Checkbox v-model="isThisLocationChecked" :binary="true" />
                                Declare this location checked
                            </div>

                        </div>

                        <div class="row" style="margin: 10px;">
                            <h1 class="h5"> Treatment (you may edit it to something special)</h1>
                            <h2 class="h5"> {{ treatmentName }}</h2>
                        </div>
                        <div class="row">
                            <div class="card flex justify-content-center text-area-parent">
                                <Textarea v-model="treatmentValue" rows="5" cols="30" disabled />
                            </div>
                        </div>
                        <div class="row">
                            <div class="submit-parent">
                                <div class="card flex justify-content-center submit-sub-parent">
                                    <Button label="Change the specific treatment" icon="pi pi-database" iconPos="right"
                                        class="submit-button" @click="updateTreatment" :disabled="isOwner" />
                                </div>
                            </div>
                        </div>
                        <div class="row" v-if="isShowSpinnerTreatments">
                            <ProgressSpinner />
                        </div>
                        <div class="row" style="margin: 10px; margin-left: 1px;" v-if="isShowTableOfTreatments">
                            <CascadeSelect v-model="selectedTreatment" :options="allTreatmentNames" optionLabel="name"
                                optionGroupLabel="name" :optionGroupChildren="['subLocations']" style="min-width: 14rem"
                                placeholder="Select a Treatment" />
                        </div>
                        <div class="row" v-if="isShowTableOfTreatments">
                            <div class="col-6">
                                <div class="submit-parent">
                                    <div class="card flex justify-content-center submit-sub-parent">
                                        <Button label="Save" icon="pi pi-check" iconPos="right" class="submit-button"
                                            @click="saveNewSpecificTreatment" :disabled="isOwner" />
                                    </div>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="submit-parent">
                                    <div class="card flex justify-content-center submit-sub-parent">
                                        <Button label="Cancel" icon="pi pi-times" iconPos="right" class="submit-button"
                                            @click="cancelSaveSpecificTreatment" :disabled="isOwner"   severity="danger"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row" v-if="isThisLocationChecked">
                            <div class="submit-parent" v-if="isThisLocationChecked">
                                <div class="card flex justify-content-center submit-sub-parent">
                                    <Button label="End this period of disease" icon="pi pi-check" iconPos="right"
                                        class="submit-button" @click="endThisPeriodOfDisease" :disabled="isOwner"
                                        severity="warning" />
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="submit-parent" v-if="!isThisLocationChecked">
                                <div class="card flex justify-content-center submit-sub-parent">
                                    <Button label="Rejct this period of disease" icon="pi pi-times-circle"
                                        iconPos="right" class="submit-button" @click="rejectThisPeriodOfDisease"
                                        :disabled="isOwner" severity="danger" />
                                </div>
                            </div>
                        </div>
                        <div>
                            <div class="row">
                                <div class="submit-parent">
                                    <div class="card flex justify-content-center submit-sub-parent">
                                        <Button label="Go to Google Maps" icon="pi pi-map" iconPos="right"
                                            class="submit-button" @click="openGoogleMapsWithLatLongLocal"
                                            severity="info" :disabled="isOwner" />
                                    </div>
                                </div>
                            </div>


                        </div>
                        <div v-if="isThisLocationChecked">


                            <hr class="header-line" style="margin:20px">
                            <div class=row>
                                <div class="col-12">
                                    <h3 class="h5" style="margin-top:20px"> Schedule treatment for this zone </h3>
                                </div>

                            </div>
                            <div class="row">
                                <div class="col-4">
                                    <hr class="header-line" style="margin-right:20px">
                                </div>
                            </div>



                            <div class="card row"
                                style="margin-left: 1px; margin-right: 3px; overflow-y: auto; max-height: 300px;">
                                <div class="col-12">
                                    <DataTable :value="scheduleData" showGridlines tableStyle="min-width: 35rem">
                                        <Column field="Date_Scheduled" header="Date"></Column>
                                        <Column header="Done">
                                            <template #body="slotProps">
                                                <span v-if="slotProps.data.Done" class="text-success">✔</span>
                                                <span v-else class="text-danger">❌</span>
                                            </template>
                                        </Column>
                                        <Column field="Farmer_Finished" header="Farmer"></Column>
                                    </DataTable>
                                </div>
                            </div>

                        </div>
                        <div class="row">
                            <div class="submit-parent" v-if="isThisLocationChecked">
                                <div class="card flex justify-content-center submit-sub-parent">
                                    <Button label="Reschedule specified treatment again" icon="pi pi-calendar-plus"
                                        iconPos="right" class="submit-button" @click="reseduleTreatmentAgain"
                                        :disabled="isOwner" severity="contrast" />
                                </div>
                            </div>
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
                        <div v-if="isShowSuccessMsg" class="row" style="margin-top: 10px; margin:10px;">
                            <Message severity="success">{{ showSuccessMsg }}</Message>
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