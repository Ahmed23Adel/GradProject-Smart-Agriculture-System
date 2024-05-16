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
import axios from "axios";

const plants = ref([]);
const days = ref();
const locations = ref();

async function get_reports() {
  await axios
    .post("http://127.0.0.1:8000/get_summary", {}, {})
    .then((res: any) => {
      plants.value = res.data.data;
    });

  days.value = [...new Set(plants.value.map((obj: any) => obj.Date))];

  locations.value = [...new Set(plants.value.map((obj: any) => obj.Location))];
}
get_reports();

const selectedDay = ref();
const selectedLocation = ref();
const status = ref();
const allComponents = [Title, ImageParagraph, Paragraph];

const components = reactive([
  {
    id: "0",
    order: 0,
    title: "The Report Title",
    imagePath: "",
    paragraph: "type the paragraph here",
    info:{}
  },
]);

function addImageParagraphComponent(id: string, path: string) {
  components.push({
    id: id,
    order: 1,
    title: "The Paragraph Title",
    imagePath: path,
    paragraph: "Type the paragraph here",
    info:{}
  });
}
let lastOrder = 0;
function addParagraphComponent() {
  lastOrder = lastOrder + 1;
  components.push({
    id: lastOrder.toString(),
    order: 2,
    title: "The Paragraph Title",
    imagePath: "",
    paragraph: "Type the paragraph here",
    info:{}
  });
}
function save() {
  let date =new Date()
  const report = { created_at:date.toDateString(),components: [] as any[] };

  for (let com of components) {
    report.components.push({
      id: com.id,
      order: com.order,
      title: com.title,
      imagePath: com.imagePath || "",
      paragraph: com.paragraph,
    });
  }

  axios.post("http://127.0.0.1:8000/add_report", report, {}).then((res) => {
   
  });
}
</script>

<template>
  <div class="report-container">
    <Sidebar class="sidebar" :selected="3" />
    <div class="summary-container">
      <div class="main-container">
        <Fliter
          :days="days"
          :locations="locations"
          @day="
            (v) => {
              v ? (selectedDay = v) : (selectedDay = v);
            }
          "
          @location="
            (v) => {
              v ? (selectedLocation = v) : (selectedLocation = v);
            }
          "
           @status="
            (v) => {
              v ? (status = v) : (status = v);
            }
          "
          class="filter"
        />
        <Results
          :plants="plants"
          :day="selectedDay"
          :location="selectedLocation"
          :status="status"
          class="results"
          @data="
            (e) => {
              addImageParagraphComponent(e.id, e.path);
             
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
          :imageid="component.imagePath"
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
        <Button label="Save" @click="save" />
        <i
          class="pi pi-plus-circle"
          @click="
            () => {
              addParagraphComponent();
            }
          "
          style="
            color: var(--accentb);
            font-size: 32px;
            display: block;
            cursor: pointer;
          "
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
  padding: 64px;
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
