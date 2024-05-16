<script lang="ts" setup>
import ResultCard from "./ResultCard.vue";
import { defineProps, ref } from "vue";

import Dialog from "primevue/dialog";
function transform(url: string) {
  const regex = /\/d\/(.*)\/view/;
  const match = url.match(regex);

  if (match) {
    const imageId = match[1];
    url = `https://drive.google.com/uc?id=${imageId}&export=download`;
  }

  url = url.replace("&export=download", "");
  url = url.replace("google", "lienuc");

  return url;
}



const props = defineProps(["day", "location", "status", "accuracy", "plants"]);
const visible = ref(false);
const selectedPlant = ref();

function test(plant: any) {
  if (props.day && plant.Date != props.day) {
    return false;
  }
  if (props.location && plant.Location != props.location) {
    return false;
  }
  console.log(props.status,plant.Image_Class)
  if (props.status && !props.status.includes(plant.Image_Class.toString())) {
    return false;
  }
  return true;
}
const classfications = ["Early Blight", "Late Blight", "Healthy"];
const editedTreated = ["No", "Yes"];

function handleImageUpload(order:number) { 
  setTimeout(() => {

    if(order==0) {
    let scaleRatioo = drawCanvasImage(order);
  
    let numberOfPoints = 0;
    let labelNumber = 0;
    let points = [];
    for (let boundingPoint of selectedPlant.value.bbox) {
      numberOfPoints = numberOfPoints + 1;
      points.push(boundingPoint);
      if (numberOfPoints == 4) {
        if (!scaleRatioo) {
          scaleRatioo = 1;
        }
        drawRectangle(
          points[0] / scaleRatioo,
          points[1] / scaleRatioo,
          points[2] / scaleRatioo,
          points[3] / scaleRatioo,
          "Leaf" + labelNumber.toString()
        );
        numberOfPoints = 0;
        points = [];
        labelNumber = labelNumber + 1;
      }
    }}
    else{
      drawCanvasImage(order);
    }
  }, 200);
};
// TODO sure it's work, I'm not sure at all
const drawCanvasImage = (order: number) => {
  const canvas = document.getElementsByClassName("canvas")[order] as HTMLCanvasElement;
  const image = document.getElementsByClassName("image")[order] as HTMLImageElement;

  if (!canvas || !image) return; // Handle potential missing canvas or image element
  const ctx = canvas.getContext("2d");
  if (!ctx) return; // Handle missing 2d context

  if (order === 0) {
    let w = image.width;
    let h = image.height;
    let ratio = Math.max(w, h) / 500;
    ctx.drawImage(image, 0, 0, w / ratio, h / ratio);

    return ratio;
  } else {
    order = order - 1;
    let sx = selectedPlant.value.bbox[order * 4];
    let sy = selectedPlant.value.bbox[order * 4 + 1];
    let sw = selectedPlant.value.bbox[order * 4 + 2];
    let sh = selectedPlant.value.bbox[order * 4 + 3];
    ctx.drawImage(image, sx, sy, sw, sh, 0, 0, 100, 100);
  }
};

const drawRectangle = (
  x: number,
  y: number,
  width: number,
  height: number,
  label: string
) => {
  const canvas = document.getElementsByClassName("canvas")[0] as HTMLCanvasElement;
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  if (!ctx) return; // Add null check for ctx

  ctx.strokeStyle = "white"; // Set stroke color
  ctx.lineWidth = 2; // Set line width
  ctx.strokeRect(x, y, width, height);

  // Draw text label
  ctx.fillStyle = "white"; // Set fill color
  ctx.font = "16px Arial"; // Set font style and size
  const textWidth = ctx.measureText(label).width; // Get text width
  ctx.fillText(label, x + (width - textWidth) / 2, y + 15); // Position text
};
</script>

<template>
  <div class="results-container">
    <div class="card-continer" v-for="plant in plants">
      <ResultCard
        @click="
          visible = true;
          selectedPlant = plant;
          
        "
        v-if="test(plant)"
        :plant="plant"
      />
    </div>
  </div>
  <Dialog
    v-model:visible="visible"
    modal
    header="Summary"
    :style="{ width: '50rem' }"
  >
    <div class="dialog-container">
      <div class="description">
        <p><strong>Location:</strong> {{ selectedPlant.Location }}</p>
        <p><strong>Date:</strong> {{ selectedPlant.Date }}</p>
        <p><strong>Time:</strong> {{ selectedPlant.Time }}</p>
        <p>
          <strong>Edited:</strong> {{ editedTreated[selectedPlant.Edited] }}
        </p>
        <p>
          <strong>Treated:</strong> {{ editedTreated[selectedPlant.Edited] }}
        </p>
        <p>
          <strong>Class:</strong>
          {{ classfications[selectedPlant.Image_Class] }}
        </p>
      </div>
      <canvas width="500" height="500" class="canvas">
        <img
          crossorigin="anonymous"
          class="image"
          :src="transform(selectedPlant.Image_Path)"
          alt=""
          @load="()=>{handleImageUpload(0)}"
        />
      </canvas>
    </div>
    <div class="classfications">
      <div class="container">
        <p v-for="(classification, i) in selectedPlant.Classification">
          <strong class="cc">Leaf:</strong> {{ i }}
        </p>
      </div>
      <div class="container">
        <p v-for="(classification, i) in selectedPlant.Classification">
          <strong>Class:</strong> {{ classfications[classification] }}
        </p>
      </div>
      <div class="container">
        <p v-for="(Confidence, i) in selectedPlant.Confidence">
          <strong>Confidence:</strong> {{ Confidence.toFixed(3) }}
        </p>
      </div>

      <div class="container">
        <canvas   v-for="(classification, i) in selectedPlant.Classification" width="100" height="100" class="canvas">
        <img
          crossorigin="anonymous"
          class="image"
          :src="transform(selectedPlant.Image_Path)"
          @load="()=>{handleImageUpload(i+1)}"
          alt=""
        />
      </canvas>
      </div>
     
    </div>
  </Dialog>
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
  justify-content: space-between;
}
.classfications {
  display: grid;
  grid-template-columns: 1fr 2fr 2fr 120px;
  margin-top: 1rem;
}
.container {
  display: grid;
  grid-template-rows: 100px;
  gap: 10px;
}
</style>
