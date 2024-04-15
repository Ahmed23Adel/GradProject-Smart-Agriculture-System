<script lang="ts" setup>
import Button from "primevue/button";
import "primeicons/primeicons.css";
import Fliter from "../components/reportspage/Filter.vue";
import Sidebar from "../components/Sidebar.vue";
import Results from "../components/reportspage/Result.vue";
import Title from "../components/reportspage/Title.vue";
import ImageParagraph from "../components/reportspage/ImageParagraph.vue";
import Paragraph from "../components/reportspage/Paragraph.vue";
import { ref, reactive } from "vue";

const selectedDay = ref();
const selectedLocation = ref();
const selectedPlant = ref();
const selectedConfedancePercentage = ref();
const selectedDiseaseCategory = ref();

const allComponents = [Title, ImageParagraph,Paragraph];
let lastElement = 0;
const components = reactive([
  {
    id: lastElement,
    order: 0,
    title: "The Report Title",
    imageid: 0,
    paragraph: "type the paragraph here",
  },
]);

function addImageParagraphComponent(id: any) {
  lastElement = lastElement + 1;
  components.push({
    id: lastElement,
    order: 1,
    title: "The Paragraph Title",
    imageid: id,
    paragraph: "Type the paragraph here",
  });
}

function addParagraphComponent() {
  lastElement = lastElement + 1;
  components.push({
    id: lastElement,
    order: 2,
    title: "The Paragraph Title",
    imageid: 0,
    paragraph: "Type the paragraph here",
  });
}
</script>

<template>
  <div class="report-container">
    <Sidebar class="sidebar" :selected="3" />
    <div class="summary-container">
      <div class="main-container">
        <Fliter
          @day="
            (v) => {
              v ? (selectedDay = v.name) : (selectedDay = v);
            }
          "
          @location="
            (v) => {
              v ? (selectedLocation = v.name) : (selectedLocation = v);
            }
          "
          @plant="
            (v) => {
              v ? (selectedPlant = v.name) : (selectedPlant = v);
            }
          "
          @disease="(v) => (selectedDiseaseCategory = v)"
          @accuracy="(v) => (selectedConfedancePercentage = v)"
          class="filter"
        />
        <Results
          :day="selectedDay"
          :location="selectedLocation"
          :plant="selectedPlant"
          :disease="selectedDiseaseCategory"
          :accuracy="selectedConfedancePercentage"
          class="results"
          @id="
            (e) => {
              addImageParagraphComponent(e);

              console.log(components);
            }
          "
        />
      </div>
    </div>

    <div class="page-area">
      <div class="report-components-wraper">
        <component
          v-for="(component, i) in components"
          :key="component.id"
          :is="allComponents[component.order]"
          :paragraph="component.paragraph"
          :imageid="component.imageid"
          :title="component.title"
          @delete="components.splice(i, 1)"
          @titleChange="
            (e) => {
              typeof e === 'string' ? (components[i].title = e) : undefined;
            }
          "
        />
       
      </div>
      <div class="action-container">
          <Button label="Save" />
          <i
            class="pi pi-plus-circle"
            @click="()=>{addParagraphComponent()}"
            style="color: var(--accentb); font-size: 32px; display: block; cursor: pointer;" 
          ></i>
      </div>
    </div>
  </div>
</template>

<style scoped>
.report-container {
  width: 100%;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: 100px 200px 1fr;
}
.summary-container {
  background-color: var(--primary);
  position: relative;
  
}
.main-container {
  display: flex;
  align-items: center;
  flex-direction: column;
  gap: 16px;
}
.sidebar {
  position: sticky;
  top: 0;
}
.page-area {
  background-color: var(--primary);

}
.report-components-wraper {
  width: 90%;
  margin-inline: auto;
  background-color: white;
  min-height: 80vh;
  margin-top: 32px;
  border-radius: 8px;
  padding: 64px
}

button {
  width: 20%;
  font-size: 24px;
  border-radius: 8px;
  height: 48px;

  background-color: var(--accentb);
}
.action-container {
  width: 90%;
  margin-inline: auto;
  padding: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 32px;

  background-color: white;
}
</style>
