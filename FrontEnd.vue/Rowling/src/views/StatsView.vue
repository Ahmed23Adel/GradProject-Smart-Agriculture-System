<script setup>
import MathsIntro from '@/components/stats/MathsIntro.vue';
import TwoFields from '@/components/stats/TwoFields.vue';
import LocationHistory from '@/components/stats/LocationHistory.vue';
import PercentageDate from '@/components/stats/PercentageDate.vue';
import ChartDateDiseased from '@/components/stats/ChartDateDiseased.vue';
import ChartDateDiseaseTypePie from '@/components/stats/ChartDateDiseaseTypePie.vue';

</script>
<template>

    <div class="container">
        <div class="childs">
            <div class="mathintro-container">
                <MathsIntro />
            </div>

            <div class="header-container">
                <div class="header-comps">
                    <h1 class="header-gen-stats">General statistics</h1>
                    <img class="header-icon" src="../assets/images/stats/icons-header.png" />
                </div>
                <hr class="header-line">

                <el-row>
                    <el-col :span="22">
                        <div clas="grid-content ep-bg-purple">
                            <h2 class="sub-header-gen-stats">From the last round:</h2>
                        </div>
                    </el-col>    
                </el-row>
                
                <TwoFields :firstField="'Percentage of diseased plants according to the model'" :secondField="'83%'"/>
                <TwoFields :firstField="'Percentage of diseased plants after modification by an expert'" :secondField="'70%'"/>
                <PercentageDate />
                <hr class="header-line-white" style="color:white;">
                <LocationHistory/>
                <hr class="header-line-white" style="color:white;">

                <hr class="header-line-white" style="color:white;">
                <ChartDateDiseased/>
                <hr class="header-line-white" style="color:white;">
                <ChartDateDiseaseTypePie/>
                <!-- <el-row>
                    <el-col :span="22">
                        <div clas="grid-content ep-bg-purple">
                            <h2 class="sub-header-gen-stats">History of certain location:</h2>
                        </div>
                    </el-col>    
                </el-row> -->

            </div>



        </div>
    </div>


</template>

<style lang="scss" scoped>
@import "../assets/scss/Stats.scss";
</style>