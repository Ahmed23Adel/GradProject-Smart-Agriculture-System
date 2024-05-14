<script setup>
import Sidebar from "../components/Sidebar.vue";
import UpperBar from "../components/treatment/UpperBar.vue";
import DefaultTreatments from "../components/treatment/DefaultTreatments.vue";
import DiseasedLocations from "../components/treatment/DiseasedLocations.vue";
import LocationHistory from '@/components/treatment/LocationHistory.vue';
import AcceptLocationsTreated from '@/components/treatment/AcceptLocationsTreated.vue';


</script>
<template>
    <div class="page-container">
        <Sidebar class="sidebar" :selected="2"/>
        <div class="main-container">
            <UpperBar/>
            <DefaultTreatments />
            <hr class="header-line">
            <DiseasedLocations/>
            <LocationHistory/>
            <hr class="header-line">
            <!-- <AcceptLocationsTreated/> -->

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