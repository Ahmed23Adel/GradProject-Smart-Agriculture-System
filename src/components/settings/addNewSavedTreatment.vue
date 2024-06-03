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
    console.log("validating input")
    console.log("headerValue.value.length", headerValue.value.length)
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
    return true;

}
async function saveNewTreatment() {
    if (validateInput()) {


        isShowLoading.value = true;
        const treatmentData = {
            treatmentName: headerValue.value,
            description: descValue.value,
            scheduleItems: scheduleNumRows.value.map(row => ({
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
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    background-color: #fff;

    th,
    td {
        border: 1px solid #ddd;
        padding: 8px;
    }

    th {
        background-color: #f2f2f2;
    }
}

.rounded-button {
    border-radius: 50px;
    /* Rounded corners */
    padding: 0.5rem 1.5rem;
    /* Adjust padding as needed */
}
</style>