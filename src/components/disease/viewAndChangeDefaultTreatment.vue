<script setup>
import { ref, onMounted, watch } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';
import { UserType } from '@/modules/Basic.ts';


const selectedDisease = ref()
const treatmentItems = ref()
const treatmentName = ref()
const treatmentDesc = ref()
const isShowChangeButton = ref(false)
const isShowLoading = ref(false)
const isInChangeMode = ref(false)
const allTreatmentNames = ref()
const selectedTreatment = ref()
const allTreatmentData = ref()

const isOwner = ref(false);

async function fetchDiseaseTreatment(disease) {
    isShowLoading.value = true
    const requester = new HttpRequester('get_saved_treatment_schedule');
    const queryParams = {
        disease_name: disease,
    };
    const requester_data = await requester.callApi('GET', queryParams);
    console.log("requester_data", requester_data)
    treatmentItems.value = requester_data.treatmentItems
    treatmentName.value = requester_data.treatmentName
    treatmentDesc.value = requester_data.treatmentDesc
    isShowLoading.value = false;
    console.log("treatmentDesc", treatmentDesc)
}

function selectDisease(disease) {
    if (!isInChangeMode.value) {
        isShowChangeButton.value = true;
        selectedDisease.value = disease;
        if (disease === "early")
            fetchDiseaseTreatment("Early blight")
        else
            fetchDiseaseTreatment("Late blight")
    }

}

async function fetchTreatmentsNames() {
    isShowLoading.value = true;
    const requester = new HttpRequester('list_saved_treatments');
    const requester_data = await requester.callApi('GET');
    allTreatmentNames.value = requester_data.saved_treatments.map(treatment => ({ name: treatment.treatmentName }));
    selectedTreatment.value = allTreatmentNames.value[0]
    allTreatmentData.value = requester_data.saved_treatments
    isShowLoading.value = false;
}
function changeDefaultTreatment() {
    fetchTreatmentsNames()
    isInChangeMode.value = true;
}

watch(selectedTreatment, (newSelectedTreatment, oldSelectedTreatment) => {
    treatmentItems.value = allTreatmentData.value
        .filter(treatment => {
            return treatment.treatmentName === newSelectedTreatment.name;
        })
        .flatMap(treatment =>
            treatment.treatment_items.map(item => ({
                dayNumber: item.dayNumber,
                dayTreatment: item.dayTreatment
            }))
        );

    console.log("treatmentItems", treatmentItems.value);
    console.log("selectedTreatmenttt", selectedTreatment.value.name)
});

async function saveNewDefaultTreatment() {
    console.log("allTreatmentData", allTreatmentData.value, selectedTreatment.value)
    isShowLoading.value = true
    const requester = new HttpRequester('update_default_saved_treatment');
    const selectedTreatmentId = allTreatmentData.value.find(treatment => treatment.treatmentName === selectedTreatment.value.name)['_id'];
    console.log("selectedTreatmentId", selectedTreatmentId)
    let selectedDiseaseFullName = "Late blight"
    // console.log("selectedDisease", selectedDisease)
    if (selectedDisease.value === "early") {
        selectedDiseaseFullName = "Early blight"
    }
    const queryParams = {
        disease_name: selectedDiseaseFullName,
        new_default_saved_treatment: selectedTreatmentId
    };
    console.log("queryParams", queryParams)
    const requester_data = await requester.callApi('PUT', queryParams);
    isShowLoading.value = false
    isInChangeMode.value = false
}
onMounted(async () => {
    isOwner.value = UserType.getInstance().getUserType();

});

</script>
<template>
    <<div id="app" class="main-container">
        <div class="row">
            <div class="col-4" @click="selectDisease('early')" :class="{ 'selected': selectedDisease === 'early' }">
                <div class="box" :style="{ 'border-color': selectedDisease === 'early' ? 'green' : 'gray' }">
                    <h1> Early blight </h1>
                </div>
            </div>
            <div class="col-4" @click="selectDisease('late')" :class="{ 'selected': selectedDisease === 'late' }">
                <div class="box" :style="{ 'border-color': selectedDisease === 'late' ? 'green' : 'gray' }">
                    <h1> Late blight </h1>
                </div>
            </div>
        </div>
        <div class="row align-items-center" v-if="!isInChangeMode">
            <Transition>
                <div class="col-4">
                    <h1>{{ treatmentName }}</h1>
                </div>
            </Transition>

            <div class="col-4" v-if="isShowChangeButton && !isOwner">
                <!-- HTML !-->
                <button class="button-74" role="button" @click="changeDefaultTreatment">Change default
                    treatment</button>
            </div>
            <div class="col-4" v-if="isShowLoading">
                <ProgressSpinner />
            </div>
        </div>
        <div class="row align-items-center" v-if="!isInChangeMode">
            <div class="col-8">
                <Textarea v-model="treatmentDesc" rows="5" cols="90" disabled  style="margin: 20px;"/>
            </div>
        </div>
        <div class="" v-if="isInChangeMode">
            <CascadeSelect v-model="selectedTreatment" :options="allTreatmentNames" optionLabel="name"
                optionGroupLabel="name" :optionGroupChildren="['subLocations']" style="min-width: 14rem"
                placeholder="Select a Treatment" />
        </div>

        <Transition>
            <div class="row">
                <table>
                    <thead>
                        <tr>
                            <th>Day Number</th>
                            <th>Treatment</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="treatmentItem in treatmentItems" :key="treatmentItem.dayNumber">
                            <td>{{ treatmentItem.dayNumber }}</td>
                            <td>{{ treatmentItem.dayTreatment }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </Transition>
        <div class="row" v-if="isInChangeMode">
            <div class="col-3">
                <div class="card flex justify-content-center submit-sub-parent">
                    <Button label="Save the updates" icon="pi pi-check" iconPos="right" class="submit-button"
                        @click="saveNewDefaultTreatment" :disabled="isOwner" />
                </div>
            </div>
        </div>


        </div>
</template>
<style lang="scss" scoped>
.page-container {
    background-color: var(--primary);
    display: grid;
    position: relative;
    grid-template-columns: 150px 1fr;
}


.sidebar {
    position: sticky;
    top: 0;
}

.math-intro-container {
    // transform: translateY(-50%);
    top: 0;
}

.box {
    border: 2px solid;
    border-radius: 50px;
    /* Rounded corners */
    margin: 30px;
    padding: 30px;
    border-width: 20px;
    cursor: pointer;
}

.selected .box {
    border-color: green;
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

.ios-change {
    color: blue;
    /* Set text color to blue */
    cursor: pointer;
    /* Change cursor to pointer */
    text-decoration: underline;
    /* Add underline */
}

.align-items-center {
    display: flex;
    align-items: center;
    /* Vertically center the items */
}

.button-74 {
    background-color: #fbeee0;
    border: 2px solid #422800;
    border-radius: 30px;
    box-shadow: #422800 4px 4px 0 0;
    color: #422800;
    cursor: pointer;
    display: inline-block;
    font-weight: 600;
    font-size: 18px;
    padding: 0 18px;
    line-height: 50px;
    text-align: center;
    text-decoration: none;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
}

.button-74:hover {
    background-color: #fff;
}

.button-74:active {
    box-shadow: #422800 2px 2px 0 0;
    transform: translate(2px, 2px);
}

@media (min-width: 768px) {
    .button-74 {
        min-width: 120px;
        padding: 0 25px;
    }
}
</style>