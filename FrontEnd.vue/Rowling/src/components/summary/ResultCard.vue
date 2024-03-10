<script lang="ts" setup>
import { defineProps } from "vue";

defineProps(["plant"]);
</script>

<template>
  <div class="card-container">
    <img :src="plant.src" alt="" />
    <p><strong>plant:</strong> {{ plant.plant }}</p>
    <p><strong>disease:</strong> {{ plant.disease }}</p>
    <p><strong>confidence:</strong> {{ plant.confidence }}</p>
    <p><strong>location:</strong>{{ plant.location }}</p>
    <p><strong>day:</strong>{{ plant.day }}</p>
  </div>
</template>

<style scoped>
.card-container {
  color: #343434;
  text-transform: capitalize;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 2px 2px 4px 4px #343434;
  line-height: 4px;
  cursor: pointer;
  margin: 12px;
}
img {
  width: 300px;
  aspect-ratio: 1/0.8;
}
strong{
    display: inline-block;
    width: 6em;
}
</style>
