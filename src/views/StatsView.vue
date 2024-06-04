<script setup>

import LocationHistory from '@/components/stats/LocationHistory.vue';
import ChartDateDiseased from '@/components/stats/ChartDateDiseased.vue';
import ChartDateDiseaseTypePie from '@/components/stats/ChartDateDiseaseTypePie.vue';
import Sidebar from "../components/Sidebar.vue";
import TodaysSummary from '@/components/stats/TodaysSummary.vue';
import UpperBar from '@/components/stats/UpperBar.vue';
import PercentageDateCard from '@/components//stats/PercentageDateCard.vue';
import Stepper from '@/components//stats/Stepper.vue';


</script>
<template>
    <div class="page-container">
        <Sidebar class="sidebar" :selected="1"/>
        <div class="main-container">
            <UpperBar/>
            <Stepper/>
            <hr class="header-line">
            <TodaysSummary/>
            <hr class="header-line">
            <PercentageDateCard />
            <hr class="header-line">
            <LocationHistory />
            <hr class="header-line">
            <ChartDateDiseased/>
            <hr class="header-line-white" style="color:white;">
            <ChartDateDiseaseTypePie/> 


        </div>
    </div>
</template>

<style lang="scss" scoped>
// @import "../assets/scss/Stats.scss";

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

.math-intro-container{
    // transform: translateY(-50%);
    top:0;
}
</style>