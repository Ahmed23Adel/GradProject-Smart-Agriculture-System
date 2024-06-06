<script lang="ts" setup>
import Fliter from "../components/summary/Filter.vue";
import Sidebar from "../components/Sidebar.vue";
import Results from "../components/summary/Results.vue";
import { ref,onMounted } from "vue";
import axios from 'axios'
import { HttpRequester } from '@/services/ApiCaller.ts';

const plants=ref([])
const days=ref()
const locations =ref()
async function get_reports(){
  const requester = new HttpRequester('get_summary');
  const requester_data = await requester.callApi('GET');
  plants.value = requester_data.summary_data
  console.log("plants.value", plants.value)

  // await axios.post('http://127.0.0.1:8000/get_summary',{},{}).then((res:any)=>{plants.value = res.data.data})
  days.value =  [...new Set(plants.value.map((obj:any) => obj.Date))];
  locations.value =  [...new Set(plants.value.map((obj:any) => obj.Location))];
}
get_reports()
const selectedDay = ref();
const selectedLocation = ref();
const status = ref();



</script>


<template>

  <div class="summary-container">
    
    <Sidebar class="sidebar" :selected="0"/>
    <div class="main-container">
      <Fliter
      :days="days"
      :locations="locations"
        @day="
          (v) => {
            (selectedDay = v) 
          }
        "
        @location="
          (v) => {
            (selectedLocation = v) 
          }
        "

@status="
          (v) => {
             (status = v) 
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
      />
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
.sidebar{
    position: sticky;
    top: 0;
}
</style>
