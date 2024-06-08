<script lang="ts" setup>
import Fliter from "../components/summary/Filter.vue";
import Sidebar from "../components/Sidebar.vue";
import Results from "../components/summary/Results.vue";
import { ref } from "vue";
import { HttpRequester } from "@/services/ApiCaller.ts";

const plants = ref([]);
const locations = ref();
const maxRange = ref();
async function get_reports() {
  const requester = new HttpRequester("get_summary");
  requester.callApi("GET").then((res) => {
    locations.value = res.all_zones;
    plants.value = res.summary_data;
    maxRange.value = res.max_index;
  });
}
get_reports();
const selectedDay = ref();
const selectedLocation = ref();
const status = ref<any[]>([]);
const selectedPage = ref();
function formatDate(dateString: string) {
  const date = new Date(dateString);
  const day = String(date.getDate()).padStart(2, "0");
  const month = String(date.getMonth() + 1).padStart(2, "0"); // Months are zero-based
  const year = date.getFullYear();
  return `${day}-${month}-${year}`;
}
function requestPlants() {
  interface dataInterface{
    selected_date:string
    selected_location:string
    is_healthy:boolean
    is_eb:boolean
    is_lb:boolean
    index:number
  }
  let data =<dataInterface>{}


  if(selectedDay.value!=undefined) { data.selected_date=formatDate(selectedDay.value)}
  if(selectedLocation.value!=undefined) {data.selected_location=selectedLocation.value}

  if(status.value!=undefined) {
    if(status.value.includes("0")){
      data.is_eb=status.value.includes("0")
    }
    if(status.value.includes("1")){
      data.is_lb=status.value.includes("1")
    }
    if(status.value.includes("2")){
      data.is_healthy=status.value.includes("2")
    }
  }
  if(selectedPage.value){
    data.index=selectedPage.value
  }
  console.log(data);
  const requester = new HttpRequester("get_summary");
  requester.callApi("GET", data).then((res) => {
    console.log(res);
    locations.value = res?.all_zones;
    plants.value = res?.summary_data;
    maxRange.value = res?.max_index;
  });
}
</script>

<template>
  <div class="summary-container">
    <Sidebar class="sidebar" :selected="0" />
    <div class="main-container">
      <Fliter
        :range="maxRange"
        :locations="locations"
        @day="
          (v) => {
            selectedDay = v;
          }
        "
        @location="
          (v) => {
            selectedLocation = v;
          }
        "
        @page="
          (v) => {
            selectedPage = v;
          }
        "
        @status="
          (v) => {
            status = v;
            requestPlants();
          }
        "
        class="filter"
      />
      <Results :plants="plants" class="results" />
    </div>
  </div>
</template>

<style scoped>
.summary-container {
  background-color: var(--primary);
  display: grid;
  position: relative;
  grid-template-columns: 150px 1fr;
}
.main-container {
  display: flex;
  align-items: center;
  flex-direction: column;
  gap: 64px;
}
.sidebar {
  position: sticky;
  top: 0;
}
</style>

{:day="selectedDay" :location="selectedLocation" :status="status"}
