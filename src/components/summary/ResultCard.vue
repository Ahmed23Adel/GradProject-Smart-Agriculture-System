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






function formatDate(dateString: string) {
  const date = new Date(dateString);
  const day = String(date.getDate()).padStart(2, "0");
  const month = String(date.getMonth() + 1).padStart(2, "0"); // Months are zero-based
  const year = date.getFullYear();
  return `${day}-${month}-${year}`;
}


</script>

<template>
 <div class="card-container">
    <img crossorigin="anonymous" :src="transform(plant.Image_Path)" alt="" />
    <p><strong>location:</strong>{{ plant.Location }}</p>
    <p><strong>day:</strong>{{ formatDate(plant.Date)}}</p>
    <p><strong>classification:</strong>{{classfications[plant.Image_Class] }}</p>
  </div>
</template>

<style scoped>
.card-container {
  color: #343434;
  text-transform: capitalize;
  padding: 16px;
  border-radius: 8px;
  background-color: var(--card);
  line-height: 4px;
  cursor: pointer;
  margin: 12px;
}
img {
  width: 300px;
  aspect-ratio: 1/0.8;
  margin-bottom: 16px;
}
strong{
    display: inline-block;
    width: 7em;
}
</style>