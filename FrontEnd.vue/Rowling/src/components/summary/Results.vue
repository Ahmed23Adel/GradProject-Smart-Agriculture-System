<script lang="ts" setup>
import ResultCard from './ResultCard.vue'; 
import plants from '@/modules/plants';
import {  defineProps } from "vue";
const props = defineProps(['day', "location", "plant", "disease", "accuracy"]);

function test(plant:any){
    if (props.day && plant.day!=props.day){
        return false
    }
    if (props.location && plant.location!=props.location){
        return false
    }
    if (props.plant && plant.plant!=props.plant){
        return false
    }
    if (props.disease=='show dieases' && plant.disease==''){
        return false
    }
    if (props.disease=='show healthy' && plant.disease!=''){
        return false
    }
    if (props.accuracy=='Accuraccy > 80' && plant.confidence<80){
        return false
    }
    if (props.accuracy=='Accuraccy < 50' && plant.confidence>50){
        return false
    }
    if (props.accuracy=='Accuraccy 50 - 80' && (plant.confidence < 50 ||  plant.confidence > 80)){
        return false
    }
    return true

}
</script>


<template>

<div class="results-container">
    <div class="card-continer" v-for="plant in plants">
    <ResultCard  v-if="test(plant)" :plant="plant"/>
    </div>
    
</div>

</template>


<style scoped>
.results-container{
   width: 95%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

</style>
