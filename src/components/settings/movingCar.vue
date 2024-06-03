<script setup>
import { ref, onMounted, watch } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';

const carCollectingImages = ref()
const imagesUploadedToTheCloud = ref()
const modelEvalResults = ref()
const resultsTransferedToDB = ref()

async function fetchCarStatus(){
    const requester = new HttpRequester('moving_car_status');
    const requester_data = await requester.callApi('GET');
    carCollectingImages.value = requester_data.carCollectingImages
    imagesUploadedToTheCloud.value = requester_data.imagesUploadedToTheCloud
    modelEvalResults.value = requester_data.modelEvalResults
    resultsTransferedToDB.value = requester_data.resultsTransferedToDB

}


onMounted(async () => {
    fetchCarStatus()
});
</script>

<template>
    <div class="row">
        <div class="col-6">
            <h4>Car is collecting images</h4>
        </div>
        <div class="col-6">
            <p class="status-not-started" v-if="carCollectingImages === 'notstarted'">Not started yet</p>
            <span class="loader" v-if="carCollectingImages === 'inprogress'"></span>
            <p class="status-done" v-if="carCollectingImages === 'done'">Done</p>
        </div>

    </div>
    <hr class="header-line">
    <div class="row">
        <div class="col-6">
            <h4>Images is being uploaded to the cloud</h4>
        </div>
        <div class="col-6">
            <p class="status-not-started" v-if="imagesUploadedToTheCloud === 'notstarted'">Not started yet</p>
            <span class="loader" v-if="imagesUploadedToTheCloud === 'inprogress'"></span>
            <p class="status-done" v-if="imagesUploadedToTheCloud === 'done'">Done</p>
        </div>
    </div>
    <hr class="header-line">
    <div class="row">
        <div class="col-6">
            <h4>Model is evaluating the results</h4>
        </div>
        <div class="col-6">
            <p class="status-not-started" v-if="modelEvalResults === 'notstarted'">Not started yet</p>
            <span class="loader" v-if="modelEvalResults === 'inprogress'"></span>
            <p class="status-done" v-if="modelEvalResults === 'done'">Done</p>
        </div>
    </div>
    <hr class="header-line">
    <div class="row">
        <div class="col-6">
            <h4>Results are being transfered to the databaes</h4>
        </div>
        <div class="col-6">
            <p class="status-not-started" v-if="resultsTransferedToDB === 'notstarted'">Not started yet</p>
            <span class="loader" v-if="resultsTransferedToDB === 'inprogress'"></span>
            <p class="status-done" v-if="resultsTransferedToDB === 'done'">Done</p>
        </div>
    </div>
    <hr class="header-line">
</template>

<style lang="scss" scoped>
.loader {
  border: 24px solid #FFF;
  border-bottom-color: #FF3D00;
  border-radius: 50%;
  display: inline-block;
  position: relative;
  box-sizing: border-box;
  animation: rotation 1s linear infinite;
}

@keyframes rotation {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
} 

.status-not-started {
  color: red; /* Text color */
  text-decoration: underline; /* Underlined text */
  font-size: 1.2em; /* Slightly bigger font size */
  font-weight: bold; /* Optional: Make the text bold */
}

.status-done {
  color: green; /* Text color */
  text-decoration: underline; /* Underlined text */
  font-size: 1.2em; /* Slightly bigger font size */
  font-weight: bold; /* Optional: Make the text bold */
}
</style>