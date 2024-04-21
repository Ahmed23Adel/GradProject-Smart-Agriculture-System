<script setup>
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import {defineProps, ref} from "vue"

const {diseaseId}  = defineProps(["diseaseId"])
const diseaseNameAbbreviation = ref()
const diseaseName = ref()
if (diseaseId == 1){
    diseaseNameAbbreviation.value = "EB"
    diseaseName.value = "Early blight"
}
else{
    diseaseNameAbbreviation.value = "LB"
    diseaseName.value = "Late blight"
}
</script>


<template>

    <div class="row">
        <div class="col-4 col-md-4 ">
            <h1 class="display-5">Treatments:{{ diseaseName }}</h1>
        </div>
        <div class="col-4 col-md-4 search-box">
            
        </div>
        <div class="col-4 col-md-4 log-in d-flex justify-content-center">
            
            <router-link to="/login"><h1 class="display-6 login-text">Login</h1></router-link>
        </div>
    </div>
</template>


<style scoped>
.header-dashboard {
    color: black;
    font-weight: bold;
    margin: 20px;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.search-box {
    padding: 20px;
}

.custom-input {
    background-color: #f5f5f5;
    color: #333;
    border-color: #ced4da;
}

.custom-btn {
    background-color: #28a745;
    color: #fff;
    border-color: #28a745;
}

.custom-btn:hover {
    background-color: #218838;
    border-color: #1e7e34;
}

.log-in {
    color: rgb(0, 204, 255);
    font-size: 30px;
    padding-top: 20px;
    font-weight: bold
}

.login-text {
    color:#5F5D9C;
    cursor: pointer;
}
</style>