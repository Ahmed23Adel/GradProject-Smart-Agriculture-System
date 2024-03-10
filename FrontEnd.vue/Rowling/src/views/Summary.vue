<script lang="ts" setup>
import Fliter from "../components/summary/Filter.vue";
import Sidebar from "../components/Sidebar.vue";
import Results from "../components/summary/Results.vue";

import { ref } from "vue";

const selectedDay = ref();
const selectedLocation = ref();
const selectedPlant = ref();
const selectedConfedancePercentage = ref();
const selectedDiseaseCategory = ref();
</script>

<template>
  <div class="summary-container">
    <Sidebar class="sidebar" />
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
../components/Sidebar.vue