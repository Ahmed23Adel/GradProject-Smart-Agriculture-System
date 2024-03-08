<script setup>
import { ref } from "vue";
import GraphOfImages from "./GraphOfImages.vue"

const selectedLocation = ref();
const locations = ref([
    {
        name: "LocationX",
        subLocations: [
            {
                cname: "(LocX21) 41°24'12.2N 2°10'26.5 E",
                cname: "(LocX22) 42°24'12.2N 2°10'26.5 E",
                cname: "(LocX23) 43°24'12.2N 2°10'26.5 E",
            }
        ]
    },
    {
        name: "LocationY",
        subLocations: [
            {
                cname: "(LocY21) 41°24'12.2N 2°10'26.5 E",
                cname: "(LocY22) 42°24'12.2N 2°10'26.5 E",
                cname: "(LocY23) 43°24'12.2N 2°10'26.5 E",
            }
        ]
    }
])

const fromDate = ref();
const toDate = ref();
</script>


<template>
    <el-row>
        <el-col :span="22">
            <div clas="grid-content ep-bg-purple">
                <h2 class="sub-header-gen-stats">History of certain location:</h2>
            </div>
        </el-col>
    </el-row>

    <div class="selectors">
        <el-row>
            <el-col :span="8" :xs="24" :sm="24" :md="24" :lg="8" :xl="8">
                <div class="grid-content ep-bg-purple">
                    <p class="pre-date" style="margin:20px"> Location </p>
                    <div class="card flex justify-content-center" style="margin:20px">
                        <CascadeSelect v-model="selectedLocation" :options="locations" optionLabel="cname"
                            optionGroupLabel="name" :optionGroupChildren="['subLocations']" style="min-width: 14rem"
                            placeholder="Select a Location" />
                    </div>
                </div>
            </el-col>

            <el-col :span="8" :xs="24" :sm="24" :md="24" :lg="8" :xl="8">
                <div class="grid-content ep-bg-purple">
                    <p class="pre-date" style="margin:20px"> From: </p>
                    <div class="card flex justify-content-center" style="margin:20px">
                        <Calendar v-model="fromDate" />
                    </div>
                </div>
            </el-col>

            <el-col :span="8" :xs="24" :sm="24" :md="24" :lg="8" :xl="8">
                <div class="grid-content ep-bg-purple">
                    <p style="margin:20px"> To: </p>
                    <div class="card flex justify-content-center" style="margin:20px">
                        <Calendar v-model="toDate" />
                    </div>
                </div>
            </el-col>

        </el-row>

        <el-row>
            <el-col :span="24">
                <div class="grid-content ep-bg-purple graph-image-parent">
                    <GraphOfImages />
                    <!-- Hello world -->
                </div>

            </el-col>
        </el-row>




    </div>



</template>

<style scoped>
.sub-header-gen-stats {
    color: black;
    left: 0%;
}

.selectors {
    /* display: flex;
    flex-direction: row; */
}

.graph-image-parent{
    display: flex;
    justify-content: center; /* Center items horizontally */
    align-items: center; /* Center items vertically */
}
</style>