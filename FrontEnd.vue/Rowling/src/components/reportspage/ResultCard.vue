<script lang="ts" setup>
import { defineProps } from "vue";

defineProps(["plant"]);
function transform(url:string){
  const regex = /\/d\/(.*)\/view/;
  const match = url.match(regex);
  
  if (match) {
    const imageId = match[1];
    url= `https://drive.google.com/uc?id=${imageId}&export=download`;
    
  } 


  url=url.replace("&export=download", "");
  url=url.replace("google", "lienuc");
  return url
}
const classfications = ["Early Blight", "Late Blight", "Healthy"];

</script>

<template>
  
  <div class="card-container">
     
    <img :src="transform(plant.Image_Path)" alt=""  crossorigin="anonymous" />
    <p><strong>location: </strong>{{ plant.Location }}</p>
    <p><strong>day:  </strong>{{ plant.Date }}</p>
    <p><strong>class:  </strong>{{ classfications[plant.Image_Class] }}</p>
  </div>
</template>

<style scoped>
.card-container {
  color: #343434;
  text-transform: capitalize;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 2px 2px 4px 4px #343434;
  line-height: 4px;
  cursor: pointer;
  margin: 12px;
}
img {
  width: 100%;
  aspect-ratio: 1/0.8;
  margin-bottom: 16px;
}
</style>