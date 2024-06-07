<template>
    <div class="stepper-container">
      <div v-for="(step, index) in steps" :key="index" class="step">
        <div
          :class="{
            'step-number': true,
            active: index === currentStep,
            completed: index < currentStep
          }"
        >
          {{ index + 1 }}
        </div>
        <div
          :class="{
            'step-description': true,
            active: index === currentStep,
            completed: index < currentStep
          }"
        >
          {{ step }}
        </div>
        <div
          v-if="index < steps.length - 1"
          :class="{
            'step-line': true,
            completed: index < currentStep
          }"
        ></div>
      </div>
    </div>
  </template>
  
  <script setup>
import { ref, watch, onMounted } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';

  // Step descriptions
  const steps = ref([
    'Car is collecting images',
    'Images are being uploaded to the cloud',
    'Model is evaluating the results',
    'Results are being transferred to the database'
  ]);
const currentStep = ref(2); // Example: the current active process is step 3

async function fetchCarStatus(){
    const requester = new HttpRequester('get_car_state');

    const requester_data = await requester.callApi('GET');
    console.log("requester_data", requester_data)
    currentStep.value = requester_data.current_state;
}
  
onMounted(async () => {
  // await fetchAllLocations(locations, selectedLocation);
  await fetchCarStatus();
});

  // Current step (0-based index)
  </script>
  
  <style scoped>
  .stepper-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 20px;
    padding: 20px;
    border-radius: 10px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  
  .step {
    display: flex;
    align-items: center;
  }
  
  .step-number {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #ccc;
    color: white;
    font-size: 18px;
    font-weight: bold;
    transition: background-color 0.3s, color 0.3s;
  }
  
  .step-description {
    margin-left: 10px;
    font-size: 16px;
    padding: 5px 10px;
    border-radius: 5px;
    transition: background-color 0.3s, color 0.3s;
  }
  
  .step-line {
    width: 50px;
    height: 2px;
    background-color: #ccc;
    margin-left: 10px;
    transition: background-color 0.3s;
  }
  
  .step-number.active,
  .step-description.active {
    background-color: #2196F3;
    color: white;
  }
  
  .step-number.completed,
  .step-line.completed {
    background-color: #4CAF50;
  }
  
  .step-description.completed {
    color: #4CAF50;
  }
  
  .step-description.active {
    background-color: #2196F3;
    color: white;
    font-weight: bold;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  
  .step-description.completed::before {
    content: '✔ ';
    color: #4CAF50;
  }
  </style>
  