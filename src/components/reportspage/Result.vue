<script lang="ts" setup>
import ResultCard from "./ResultCard.vue";
import { defineProps, ref } from "vue";

function transform(url: string) {
  url = url.replace("$export=download", "");
  url = url.replace("/uc?", "/thumbnail?");
  return url;
}
const props = defineProps(["day", "location", "status", "accuracy", "plants"]);


function test(plant: any) {
  if (props.day && plant.Date != props.day) {
    return false;
  }
  if (props.location && plant.Location != props.location) {
    return false;
  }
  if (props.status && !props.status.includes(plant.Image_Class.toString())) {
    return false;
  }
  return true;
}
const emit =defineEmits(['data'])
</script>

<template>
  <div class="results-container">
    <div class="card-continer" v-for="plant in plants">
      <ResultCard
        @click="
        ()=>{
        $emit('data',{id:plant._id,path:plant.Image_Path})}
        "
        v-if="test(plant)"
        :plant="plant"
      />
    </div>
  </div>

</template>

<style scoped>
.results-container {
  width: 95%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.dialog-container {
  display: flex;
  justify-content: space-between
}
img {
  width: 20rem;
  aspect-ratio: 1.0/0.8;
  border-radius: 4px;
}
.description {
  width: 10rem;
}
.classfications{
    display: grid;
    grid-template-columns: 1fr 2fr 2fr;
    margin-top: 1rem;
}
</style>
