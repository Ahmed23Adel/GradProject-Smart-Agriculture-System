<script lang="ts" setup>
import "primeicons/primeicons.css";
import { defineProps,ref } from "vue";
import { useRouter } from "vue-router";
const router =useRouter()

defineProps(['selected'])
const fullWidth =ref(true)
</script>

<template>
  <div class="wrapper">
    <i class="pi pi-list" @click="fullWidth=!fullWidth" style="color: var(--accenta);cursor: pointer;"></i>
    <div class="sidebar-container" :class="{small:!fullWidth}">
      <div class="today-summary"  :class="{ selected: selected == 0 }" @click="router.push('summary')">
        <i class="pi pi-calendar"></i>
        <p>summary</p>
      </div>
      <div class="statistics" :class="{ selected: selected == 1 }" @click="router.push('stats')">
        <i class="pi pi-chart-bar"></i>
        <p>statistics</p>
      </div>
      <div class="treatment" :class="{ selected: selected == 2 }" @click="">
        <i class="pi pi-briefcase"></i>
        <p>treatments</p>
      </div>
      <div class="reports" :class="{ selected: selected == 3 }" @click=""> 
        <i class="pi pi-file"></i>
        <p>reports</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
* {
  margin: 0;
  padding: 0;
  font-size: 12px;
}
.wrapper{
    padding-left: 8px;
    background-color: var(--secondary);
    width: fit-content;
    height: 100vh;
    position: sticky;
}
.sidebar-container {
  height: 100vh;
  width: 120px;
  background-color: var(--secondary);
  color: var(--accenta);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 64px;
  gap: 16px;
  overflow: hidden;
  transition-duration: 0.5s;
}
.small{
    width:60px
}
.sidebar-container > * {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 16px;
  margin: 0;
  padding: 0;
  cursor: pointer;
  text-transform: capitalize;
  width: 100%;
  padding-block: 8px;
  padding-inline: 16px;
  position: relative;
}
.selected {
  background-color: var(--primary);
  color: var(--accenta);
  border-bottom-left-radius: 32px;
  border-top-left-radius: 32px;
}
.selected::after {
  content: "";
  width: 16px;
  height: 16px;
  background-color: transparent;
  position: absolute;
  right: 0;
  top: 0;
  transform: translate(-0, -16px);
  border-bottom-right-radius: 100%;
  box-shadow: 8px 8px 0 8px var(--primary);
}
.selected::before {
  content: "";
  width: 16px;
  height: 16px;
  background-color: transparent;
  position: absolute;
  right: 0;
  bottom: 0;
  transform: translate(-0, 16px);
  border-top-right-radius: 100%;
  box-shadow: 8px -8px 0 8px var(--primary);
}
.selected>i{
    background-color: var(--secondary);
    border-radius: 100%;
}
i{
    padding: 8px;
}
</style>
