<script setup>
import viewAndChangeDefaultTreatment from "../components/disease/viewAndChangeDefaultTreatment.vue"
import addNewSavedTreatment from "../components/disease/addNewSavedTreatment.vue"
import viewAndEditSavedTreatments from "../components/disease/viewAndEditSavedTreatments.vue"
import Sidebar from "../components/Sidebar.vue";
import { UserType } from '@/modules/Basic.ts';
import { ref, onMounted, watch } from "vue";

const isOwner = ref(false)
onMounted(async () => {
    isOwner.value = UserType.getInstance().getUserType();
});
</script>

<template>

<div class="page-container">
        <Sidebar class="sidebar" :selected="7" />
        <div class="main-container">
            <viewAndChangeDefaultTreatment/>
            <hr class="header-line">
            <viewAndEditSavedTreatments/>
            <hr class="header-line">
            <addNewSavedTreatment v-if="!isOwner"/>
            <hr class="header-line">
            <movingCar/>
        </div>
    </div>
</template>


<style lang="scss" scoped>
.page-container {
    background-color: var(--primary);
    display: grid;
    position: relative;
    grid-template-columns: 150px 1fr;
}


.sidebar {
    position: sticky;
    top: 0;
}

.math-intro-container {
    // transform: translateY(-50%);
    top: 0;
}

</style>