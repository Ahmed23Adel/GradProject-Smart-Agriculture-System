<script setup>
import Sidebar from "../components/Sidebar.vue";
import UpperBar from "../components/treatment/UpperBar.vue";
import DefaultTreatments from "../components/treatment/DefaultTreatments.vue";


</script>
<template>
    <div class="page-container">
        <Sidebar class="sidebar" :selected="2"/>
        <div class="main-container">
            <UpperBar/>
            <DefaultTreatments />

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