<script setup>
import { useRoute } from 'vue-router';
import Sidebar from "../components/Sidebar.vue";
import UpperBarDisesae from "../components/treatment/UpperBarDisesae.vue";
import { ref, onMounted } from "vue"
import { HttpRequester } from '@/services/ApiCaller.ts';
import Cookies from 'js-cookie';
import { UserType } from '@/modules/Basic.ts';


const route = useRoute()
const diseaseId = route.params['id']
const treatmentValue = ref("")
treatmentValue.value = ""
const isOwner = ref(false);
const isShowLoadingSaveUpdates = ref(false)
const isShowErrorMsg = ref(false)
const errorMessage = ref("Error happened while performing this action. Please try again")

async function fetchDefaultTreatment(){
    const requester = new HttpRequester('get-default-treatment');
    const requester_data = await requester.callApi('GET');
    if (diseaseId==1){
        treatmentValue.value = requester_data.Early_Blight
    }
    else{
        treatmentValue.value = requester_data.Late_Blight
    }
    // TODO Make sure that this is its treatemtn
}

async function saveUpdates(){
    isShowLoadingSaveUpdates.value = true;
    isShowErrorMsg.value = false;
    const requester = new HttpRequester('update-default-treatment');
    let diseaseNameAbbreviation = ""
    if (diseaseId == 1){
        diseaseNameAbbreviation = "Early_Blight"
    }
    else{
        diseaseNameAbbreviation = "Late_Blight"
    }
    const queryParams = {
        diseaesName: diseaseNameAbbreviation,
        treatment: treatmentValue.value,
    };
    const requester_data = await requester.callApi('PUT', queryParams);
    console.log("requester_data", requester_data)
    if (requester_data === false){
        isShowErrorMsg.value = true;
        errorMessage.value = "Error saving your updates. Please try again"
    }
    isShowLoadingSaveUpdates.value = false;
}


onMounted(async () => {
    isOwner.value = UserType.getInstance().getUserType();   
    console.log("isowner", isOwner.value);
    await fetchDefaultTreatment();
     
});


</script>
<template>
    <div class="page-container">
        <Sidebar class="sidebar" :selected="2" />
        <div class="main-container">
            <UpperBarDisesae :diseaseId=diseaseId />
            <div class="row">
                <img src="/src/assets/images/diseaseDefaultTreatment/background.jpg" alt="Description of the image"
                    class="full-width-image">
            </div>
            <div class="row">
                <h1 class="display-6">Default treatment:</h1>
            </div>
            <div class="card flex justify-content-center text-area-parent">
                <Textarea v-model="treatmentValue" rows="5" cols="30" />
            </div>
            <div class="submit-parent">
                <div class="card flex justify-content-center submit-sub-parent">
                    <Button label="Save the updates" icon="pi pi-check" iconPos="right" class="submit-button" @click="saveUpdates" :disabled="isOwner"/>
                </div>
                
            </div>
            <div v-if="isShowLoadingSaveUpdates" class="row">
                    <ProgressSpinner />
            </div>
            <div v-if="isShowErrorMsg" class="row" style="margin-top: 10px; margin:10px;">
                <Message severity="error" >{{ errorMessage }}</Message>
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

.full-width-image {
    width: 100%;
    height: 500px;
    object-fit: cover;
    border-radius: 100px;

}

.text-area-parent {
    margin-right: 50px;
}

.submit-parent {
    display: flex;
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    margin-top: 30px;
    background-color: var(--primary);
}

.submit-button{
    border-radius: 20px;
}

.submit-sub-parent{
    background-color: var(--primary);
    border: none;
}
</style>