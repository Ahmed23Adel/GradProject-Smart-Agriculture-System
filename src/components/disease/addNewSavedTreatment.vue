<script setup>
import { ref, onMounted, watch } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';

const headerValue = ref("")
const descValue = ref("")
const scheduleNumRows = ref([{ dayNumber: "", dayTreatment: "" }]);
const isShowLoading = ref(false)
const isShowSuccess = ref(false)
const isShowError = ref(false)
const successMsg = ref("")
const errorMsg = ref("")

function addRow() {
    scheduleNumRows.value.push({ dayNumber: "", dayTreatment: "" });
}

function removeRow(index) {
    scheduleNumRows.value.splice(index, 1);
}

function validateInput() {
    if (headerValue.value.length < 3) {
        isShowError.value = true;
        errorMsg.value = "Value of header must be at least 3 characters"
        return false;
    }
    if (descValue.value.length < 3) {
        isShowError.value = true;
        errorMsg.value = "Value of description must be at least 3 characters"
        return false;
    }
    if (scheduleNumRows.value < 1) {
        isShowError.value = true;
        errorMsg.value = "You must have at least one day treatment in schedule"
        return false;
    }
    if (scheduleNumRows.value > 30) {
        isShowError.value = true;
        errorMsg.value = "At the current momeent, you can't have more than 30 days treatment in schedule"
        return false;
    }
    console.log("scheduleNumRows",scheduleNumRows)
    if (!scheduleNumRows.value.every((item) => item.dayNumber >= 1)) {
        isShowError.value = true;
        errorMsg.value = "There is a day number < 1"
        console.log("error")
        return false; // Missing dayNumber or dayTreatment
    }
    if (!scheduleNumRows.value.every((item) => item.dayTreatment !== "")) {
        isShowError.value = true;
        errorMsg.value = "All treatment items must be filled"
        console.log("error")
        return false; // Missing dayNumber or dayTreatment
    }
    const dayNumbers = new Set(scheduleNumRows.value.map((item) => item.dayNumber));
    if (dayNumbers.size !== scheduleNumRows.value.length) {
        isShowError.value = true;
        errorMsg.value = "Duplicated day numbers"
        return false; // Duplicate dayNumbers found
    }
    const sortedDayNumbers = [...dayNumbers].sort((a, b) => a - b);
    if (!scheduleNumRows.value.every((item, index) => item.dayNumber === sortedDayNumbers[index])) {
        isShowError.value = true;
        errorMsg.value = "Day numbers must be in order"
        return false; // Items not ordered correctly
    }

    return true;

}
function cleanInputFields(){
    headerValue.value = ""
    descValue.value = 
    scheduleNumRows.value = ""
    isShowLoading.value =  false
    isShowSuccess.value = false
    isShowError.value = false
}
async function saveNewTreatment() {
    if (validateInput()) {
        isShowLoading.value = true;
        const treatmentData = {
            treatmentName: headerValue.value,
            treatmentDescription: descValue.value,
            treatmentItems: scheduleNumRows.value.map(row => ({
                dayNumber: row.dayNumber,
                dayTreatment: row.dayTreatment
            }))
        };

        console.log("Treatment Data:", treatmentData);
        const requester = new HttpRequester('create_saved_treatment_schedule');
        const requester_data = await requester.callApi('POST', null, treatmentData);
        if (requester_data) {
            isShowSuccess.value = true;
            isShowError.value = false;
            successMsg.value = "Saved your treatment schedule"
            cleanInputFields()
        } else {
            isShowSuccess.value = false;
            isShowError.value = true;
            errorMsg.value = "Could not saved your treatment schedul. Please try again later"
        }
        isShowLoading.value = false;
    }
}
</script>
<template>
    <h1 style="margin: 20px;"> Add new saved treatment</h1>
    <h3>Header: </h3>
    <div class="row">
        <div class="col-8">
            <InputText type="text" v-model="headerValue" class="inputLabl" />
        </div>
    </div>


    <h3 style="margin-top: 10px;">Description: </h3>
    <div class="row">
        <div class="col-8">
            <Textarea v-model="descValue" rows="5" cols="80" />

        </div>
    </div>

    <h3>Schedule: </h3>
    <table>
        <thead>
            <tr>
                <th>Day Number</th>
                <th>Treatment</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(row, index) in scheduleNumRows" :key="index">
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
    <Button @click="addRow" label="Add Row" class="p-button-success rounded-button" />

    <div class="row" style="margin-top: 20px;">
        <div class="col-3">
            <Button @click="saveNewTreatment" label="Save new treatment" class="p-button-success rounded-button" />
        </div>
        <div class="col-3" v-if="isShowLoading">
            <ProgressSpinner />
        </div>

    </div>
    <div class="text-center">
        <Message severity="success" v-if="isShowSuccess">{{ successMsg }}</Message>
        <Message severity="error" v-if="isShowError">{{ errorMsg }}</Message>
    </div>

</template>

<style lang="scss" scoped>
.inputLabl {
    min-width: 80%;
}


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