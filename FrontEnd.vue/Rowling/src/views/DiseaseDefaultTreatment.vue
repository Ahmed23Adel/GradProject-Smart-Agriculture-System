<script setup>
import { useRoute } from 'vue-router';
import Sidebar from "../components/Sidebar.vue";
import UpperBarDisesae from "../components/treatment/UpperBarDisesae.vue";
import { ref } from "vue"

const route = useRoute()
const diseaseId = route.params['id']

const treatmentValue = ref("")
treatmentValue.value = "Cover the soil under the plants with mulch, such as fabric, straw, plastic mulch, or dried leaves. Water at the base of each plant, using drip irrigation, a soaker hose, or careful hand watering. Pruning the bottom leaves can also prevent early blight spores from splashing up from the soil onto leaves."
</script>
<template>
    <div class="page-container">
        <Sidebar class="sidebar" :selected="2" />
        <div class="main-container">
            <UpperBarDisesae :diseaseName="'Early blight'" />
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
                    <Button label="Save the updates" icon="pi pi-check" iconPos="right" class="submit-button" />
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