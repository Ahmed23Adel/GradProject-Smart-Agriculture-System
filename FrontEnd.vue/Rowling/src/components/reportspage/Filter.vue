<script lang="ts" setup>
import Dropdown from "primevue/dropdown";
import RadioButton from "primevue/radiobutton";
import Button from "primevue/button";

import { ref, defineEmits } from "vue";

const selectedDay = ref();
const selectedLocation = ref();
const selectedPlant = ref();
const selectedConfedancePercentage = ref();
const selectedDiseaseCategory = ref();

const options = ref([
  {
    name: "Days",
    selections: [
      { name: "20-4-2020" },
      { name: "21-4-2020" },
      { name: "22-4-2020" },
    ],
    var: selectedDay,
  },
  {
    name: "Locations",
    selections: [{ name: "Area0" }, { name: "Area1" }, { name: "Area2" }],
    var: selectedLocation,
  },
  {
    name: "Plants",
    selections: [{ name: "Potato" }, { name: "Tomato" }, { name: "Carot" }],
    var: selectedPlant,
  },
]);

const options2 = ref([
  {
    name: "Disease",
    selections: [
      { name: "show dieases" },
      { name: "show healthy" },
      { name: "show both" },
    ],
    var: selectedDiseaseCategory,
  },
  {
    name: "Accuracy",
    selections: [
      { name: "Accuraccy > 80" },
      { name: "Accuraccy 50 - 80" },
      { name: "Accuraccy < 50" },
    ],
    var: selectedConfedancePercentage,
  },
]);

const emit = defineEmits(["day", "location", "plant", "disease", "accuracy"]);
function emitSelections() {
  emit("day", selectedDay.value);
  emit("location", selectedLocation.value);
  emit("plant", selectedPlant.value);
  emit("disease", selectedDiseaseCategory.value);
  emit("accuracy", selectedConfedancePercentage.value);
}
</script>

<template>
  <div class="filter-container">
    <div class="dropdown-container">
      <div v-for="option in options" class="options-container">
        <Dropdown
          style="width: 100%"
          class="dropdown"
          :options="option.selections"
          optionLabel="name"
          :placeholder="option.name"
          v-model="option.var"
          :maxSelectedLabels="1"
          :pt="{
            wrapper: { style: { backgroundColor: 'var(--secondary)'} },
            input: { style: { color: 'var(--accenta)',fontSize:'12px',paddingBlock:'4px' } },
            item: { style: { color: 'var(--accenta)' } },
          }"
        />
      </div>
    </div>
    <div class="optin-container" v-for="option in options2">
      <div v-for="selection in option.selections">
        <RadioButton
          v-model="option.var"
          :inputId="selection.name"
          class="radiobutton"
          name="dynamic"
          :value="selection.name"
          :pt="{
            box: { style: { backgroundColor: 'var(--transparent)' } },
            icon: { style: { backgroundColor: 'var(--accenta)' } },
            root: { style: { backgroundColor: 'white', borderRadius:'100%',border:'5px'} },
            input: { style: { backgroundColor: 'var(--accenta)' } },
          }"
        />
        <label style="color: var(--accenta)" class="ml-2">{{
          selection.name
        }}</label>
      </div>
    </div>
    <Button @click="emitSelections" label="Apply Filter" />
  </div>
</template>

<style scoped>
.filter-container {
  padding-top: 16px;
  width: 90%;
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-inline: auto;
  font-size: 12px;
}
.dropdown-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.options-container {
  width: 100%;
}
.dropdown {
  height: 25px;
  background-color: var(--secondary);
  color: var(--accenta);
  font-size: 12px;
}
.optin-container {
  width: 90%;
  margin-inline: auto;
  display: grid;
  grid-template-rows: 1fr 1fr 1fr;
}
.optin-container > * {
  margin: 0px;
  display: flex;
  align-items: start;
  justify-content: start;
  gap: 8px;
}
button {
  width: 80%;
  margin-inline: auto;
  background-color: var(--accentb);
  height: 20px;
  border-radius: 8px;
}
</style>
