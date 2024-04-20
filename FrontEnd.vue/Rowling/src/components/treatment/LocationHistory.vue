<script setup>
import { ref } from "vue";
import GraphOfImagesTreatment from "./GraphOfImagesTreatment.vue"

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
    
    <div class="selectors">
        <el-row>
            <el-col :span="8" :xs="24" :sm="24" :md="24" :lg="8" :xl="8">
                <div class="grid-content ep-bg-purple">
                    <div class="card flex justify-content-center" style="margin:20px">
                        <CascadeSelect v-model="selectedLocation" :options="locations" optionLabel="cname"
                            optionGroupLabel="name" :optionGroupChildren="['subLocations']" style="min-width: 14rem"
                            placeholder="Select a Location" />
                    </div>
                </div>
            </el-col>
        </el-row>

        <div class="row" >
            <div class="col-12">
                <!-- <div class="grid-content ep-bg-purple graph-image-parent"> -->
                    <GraphOfImagesTreatment />
                <!-- </div> -->

            </div>
        </div>




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

.graph-image-parent {
    display: flex;
    justify-content: center;
    /* Center items horizontally */
    align-items: center;
    /* Center items vertically */
}

.pre-date {
    font-size: 28px;
}
</style>