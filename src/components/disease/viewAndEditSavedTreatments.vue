Copy code
<script setup>
import { ref, onMounted, watch } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';
import { UserType } from '@/modules/Basic.ts';

const allTreatmentNames = ref([]);
const selectedTreatment = ref();
const isOwner = ref(true);
const isShowLoading = ref(false);
const treatmentName = ref("treatment name");
const treatmentDescription = ref("treatment description");
const isAnyThingChanged = ref(true);
const treatmentItems = ref([]);
const allTreatmentData = ref([]);
const isShowError = ref(false);
const errorMsg = ref("");
const isShowSuccess = ref(false);
const successMsg = ref("");
const isDeleteLoading = ref(false);
let counterDescChanged = 0;

async function fetchAllSavedTreatments(disease) {
    isShowLoading.value = true;
    const requester = new HttpRequester('get_all_treatments_and_schedules');
    const requester_data = await requester.callApi('GET');
    console.log("requester_data", requester_data);
    allTreatmentNames.value = requester_data.saved_treatments.map(treatment => ({ name: treatment.treatmentName }));
    allTreatmentData.value = requester_data.saved_treatments;
    selectedTreatment.value = allTreatmentNames.value[0];
    isShowLoading.value = false;
}

function addRow() {
    console.log("addRow");
    for (let i = 0; i < allTreatmentData.value.length; i++) {
        let currentTreatment = allTreatmentData.value[i];
        if (currentTreatment.treatmentName === selectedTreatment.value.name) {
            currentTreatment.treatmentItems.push({ dayNumber: 1, dayTreatment: "" });
        }
    }
}

function removeRow(index) {
    const matchingTreatmentIndex = allTreatmentData.value.findIndex(
        (treatment) => treatment.treatmentName === selectedTreatment.value.name
    );

    if (matchingTreatmentIndex !== -1) {
        // Treatment found, remove the item at the given index
        allTreatmentData.value[matchingTreatmentIndex].treatmentItems.splice(index, 1);
        console.log("Item removed from treatment");
        // isAnyThingChanged.value = true;
    } else {
        console.log("Treatment not found");
    }
}

function validateInput() {
    // Check if a treatment is selected (assuming selectedTreatment has a value)
    if (!selectedTreatment.value) {
        return false; // No treatment selected
    }

    const selectedTreatmentData = allTreatmentData.value.find(
        (treatment) => treatment.treatmentName === selectedTreatment.value.name
    );
    console.log("selectedTreatmentData", selectedTreatmentData);
    if (!selectedTreatmentData) {
        return false; // Treatment not found in allTreatmentData
    }

    const treatmentItems = selectedTreatmentData.treatmentItems;
    console.log("treatmentItems", treatmentItems);
    // Check if all items have dayNumber >= 1 and dayTreatment != ""
    if (!treatmentItems.every((item) => item.dayNumber >= 1)) {
        isShowError.value = true;
        errorMsg.value = "There is a day number < 1";
        console.log("error");
        return false; // Missing dayNumber or dayTreatment
    }
    if (!treatmentItems.every((item) => item.dayTreatment !== "")) {
        isShowError.value = true;
        errorMsg.value = "All treatment items must be filled";
        console.log("error");
        return false; // Missing dayNumber or dayTreatment
    }
    // Check for duplicate dayNumbers
    const dayNumbers = new Set(treatmentItems.map((item) => item.dayNumber));
    if (dayNumbers.size !== treatmentItems.length) {
        isShowError.value = true;
        errorMsg.value = "Duplicated day numbers";
        return false; // Duplicate dayNumbers found
    }

    // Check for order (1, 3, 4, ...)
    const sortedDayNumbers = [...dayNumbers].sort((a, b) => a - b);
    if (!treatmentItems.every((item, index) => item.dayNumber === sortedDayNumbers[index])) {
        isShowError.value = true;
        errorMsg.value = "Day numbers must be in order";
        return false; // Items not ordered correctly
    }

    return true; // All validation conditions met
}

async function saveChanges() {
    console.log("save changes");
    if (validateInput()) {
        const selectedTreatmentData = allTreatmentData.value.find(
            (treatment) => treatment.treatmentName === selectedTreatment.value.name
        );
        console.log("saveChanges:: selectedTreatmentData", selectedTreatmentData, treatmentDescription.value);
        selectedTreatmentData.treatmentDescription = treatmentDescription.value;
        const requester = new HttpRequester('update_saved_treatment_schedule/' + selectedTreatmentData.treatmentName);
        const requester_data = await requester.callApi('PUT', null, selectedTreatmentData);
        if (requester_data) {
            isShowSuccess.value = true;
            successMsg.value = "Treatment updated successfully";
        }
    }
}

watch([selectedTreatment], async ([newSelectedTreatment], [oldSelectedTreatment]) => {
    for (let i = 0; i < allTreatmentData.value.length; i++) {
        let cur_treatment = allTreatmentData.value[i];
        if (cur_treatment.treatmentName === newSelectedTreatment.name) {
            treatmentItems.value = cur_treatment.treatmentItems;
            treatmentDescription.value = cur_treatment.treatmentDescription;
        }
    }
});

async function deleteSavedTreatment() {
    isDeleteLoading.value = true;
    const treatmentName = selectedTreatment.value.name;
    const requester = new HttpRequester(`delete_saved_treatment_schedule/${treatmentName}`);
    try {
        const response = await requester.callApi('DELETE');
        if (response) {
            isShowSuccess.value = true;
            successMsg.value = "Treatment deleted successfully";
            // Optionally, you can remove the deleted treatment from the local data
            const index = allTreatmentData.value.findIndex(treatment => treatment.treatmentName === treatmentName);
            if (index !== -1) {
                allTreatmentData.value.splice(index, 1);
                allTreatmentNames.value.splice(index, 1);
                if (allTreatmentNames.value.length > 0) {
                    selectedTreatment.value = allTreatmentNames.value[0];
                } else {
                    selectedTreatment.value = null;
                }
            }
        }
    } catch (error) {
        console.error("Error deleting treatment:", error);
        isShowError.value = true;
        errorMsg.value = "Failed to delete the treatment";
    } finally {
        isDeleteLoading.value = false;
    }
}

onMounted(async () => {
    isOwner.value = UserType.getInstance().getUserType();
    fetchAllSavedTreatments();
});
</script>

<template>
    <div v-if="!isOwner">
        <h1>View, edit, and delete saved treatments</h1>
    </div>
    <div v-if="isOwner">
        <h1>View saved treatments</h1>
    </div>
    <div class="row" style="margin: 20px;">
        <CascadeSelect v-model="selectedTreatment" :options="allTreatmentNames" optionLabel="name"
            optionGroupLabel="name" :optionGroupChildren="['subLocations']" style="min-width: 14rem"
            placeholder="Select a Treatment" />
    </div>
    <div class="row">
        <h1> Description </h1>
    </div>
    <div class="row">
        <div class="col-8">
            <Textarea v-model="treatmentDescription" rows="5" cols="70" style="margin: 20px;" />
        </div>
    </div>
    <table style="margin: 20px;">
        <thead>
            <tr>
                <th>Day Number</th>
                <th>Treatment</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(row, index) in treatmentItems" :key="index">
                <td>
                    <InputText v-model="row.dayNumber" type="number" />
                </td>
                <td>
                    <InputText v-model="row.dayTreatment" type="text" />
                </td>
                <td>
                    <Button @click="removeRow(index)" label="Delete" class="p-button-danger rounded-button" />
                </td>
            </tr>
        </tbody>
    </table>
    <Button @click="addRow" label="Add Row" class="p-button-success rounded-button" style="margin: 20px;" />
    <div class="row" style="margin: 20px;" v-if="!isOwner">
        <div class="col-4">
            <div class="card flex justify-content-center submit-sub-parent">
                <Button label="Save the updates" icon="pi pi-check" iconPos="right" class="submit-button"
                    @click="saveChanges" :disabled="isOwner || (!isOwner && !isAnyThingChanged)" />
            </div>
        </div>
        <div class="col-4">
            <div class="card flex justify-content-center submit-sub-parent">
                <Button label="Delete this saved treatment" icon="pi pi-check" iconPos="right" class="submit-button"
                    @click="deleteSavedTreatment"
                    :disabled="isOwner || (!isOwner && !isAnyThingChanged) || isDeleteLoading" />
            </div>
        </div>
    </div>
    <!-- <Message severity="error" v-if="isShowError">{{ errorMsg }}</Message> -->
    <div class="alert alert-danger" role="alert" v-if="isShowError">
        {{ errorMsg }}
    </div>
    <div class="alert alert-success" role="alert" v-if="isShowSuccess">
        {{ successMsg }}
    </div>
</template>

<style type="text/css">
table {
    max-width: 100%;
    width: 100%;
    font-family: 'Arial';
    margin: 25px auto;
    border-collapse: collapse;
    border: 1px solid #eee;
    border-bottom: 2px solid #00cccc;
    box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.10),
        0px 10px 20px rgba(0, 0, 0, 0.05),
        0px 20px 20px rgba(0, 0, 0, 0.05),
        0px 30px 20px rgba(0, 0, 0, 0.05);

    tr {
        &:hover {
            background: #f4f4f4;

            td {
                color: #555;
            }
        }
    }

    th,
    td {
        color: #424242;
        border: 1px solid #eee;
        padding: 12px 35px;
        border-collapse: collapse;
    }

    th {
        background: #00cccc;
        color: #fff;
        text-transform: uppercase;
        font-size: 12px;

        &.last {
            border-right: none;
        }
    }
}

.rounded-button {
    border-radius: 50px;
    /* Rounded corners */
    padding: 0.5rem 1.5rem;
    /* Adjust padding as needed */
}
</style>