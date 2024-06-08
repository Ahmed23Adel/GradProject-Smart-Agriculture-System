<script lang="ts" setup>
import Dropdown from "primevue/dropdown";
import Button from "primevue/button";
import Checkbox from "primevue/checkbox";

import { ref, defineEmits } from "vue";

const selectedDay = ref();
const selectedLocation = ref();
const status = ref();
const prop = defineProps(["locations", "days"]);

const emit = defineEmits(["day", "location", "status"]);
function emitSelections() {
  emit("day", selectedDay.value);
  emit("location", selectedLocation.value);
  emit("status", status.value);
}
</script>

<template>
  <div class="filter-container">
    <div class="dropdown-container">
      <Dropdown
        style="width: 100%"
        class="dropdown"
        :options="days"
        optionLabel=""
        placeholder="Date"
        v-model="selectedDay"
        :maxSelectedLabels="1"
        :pt="{
          wrapper: { style: { backgroundColor: 'var(--secondary)' } },
          input: { style: { color: 'var(--text)' ,fontWeight: 'bold'} },
          item: { style: { color: 'var(--text)' ,fontWeight: 'bold'} },
        }"
      />
      <Dropdown
        style="width: 100%"
        class="dropdown"
        :options="locations"
        optionLabel=""
        placeholder="Location"
        v-model="selectedLocation"
        :maxSelectedLabels="1"
        :pt="{
          wrapper: { style: { backgroundColor: 'var(--secondary)' } },
          input: { style: { color: 'var(--text)' ,fontWeight: 'bold'} },
          item: { style: { color: 'var(--text)',fontWeight: 'bold' } },
        }"
      />
    </div>

    <div class="checkbox">
      <div class="flex">
        <Checkbox
          v-model="status"
          inputId="ingredient1"
          name="pizza"
          value="2"
        />
        <label for="ingredient1" class="ml-2"> Healthy </label>
      </div>
      <div class="flex">
        <Checkbox
          v-model="status"
          inputId="ingredient2"
          name="pizza"
          value="0"
        />
        <label for="ingredient2" class="ml-2"> Early Blight </label>
      </div>
      <div class="flex">
        <Checkbox
          v-model="status"
          inputId="ingredient3"
          name="pizza"
          value="1"
        />
        <label for="ingredient3" class="ml-2"> Late Blight </label>
      </div>
    </div>
    <Button @click="emitSelections" label="Apply Filter" />
  </div>
</template>

<style scoped>
.filter-container {
  padding-top: 32px;
  width: 90%;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.dropdown {
  background-color: var(--secondary);
  color: var(--accenta);
  width: 30%;
}
.dropdown-container {
  width: 100%;
  margin-inline: auto;
}
button {
  width: 80%;
  margin-inline: auto;
  background-color: var(--accentb);
}
</style>
