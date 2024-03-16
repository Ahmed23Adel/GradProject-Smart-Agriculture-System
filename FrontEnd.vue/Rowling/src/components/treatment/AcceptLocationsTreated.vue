<script setup>
import { ref } from "vue";
import GraphOfImages from "../stats/GraphOfImages.vue"

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
    <h1 class="h3">Accept these locations are finished</h1>
    <h1 class="h6">These locations need your approval: </h1>

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

    <div class="row graph-parent">
        <div class="col-6 graph-parent">
            <GraphOfImages />
        </div>
        <div class="col-6">
            <div class="submit-parent">
                <div class="card flex justify-content-center submit-sub-parent">
                    <Button label="Accept treated" icon="pi pi-check" iconPos="right" class="submit-button" />
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.graph-parent {
    background-color: var(--primary);
}

.submit-parent {
    display: flex;
    justify-content: center;
    /* Center horizontally */
    align-items: center;
    /* Center vertically */
    margin-top: 30px;
    background-color: var(--primary);
}

.submit-button {
    border-radius: 20px;
}

.submit-sub-parent {
    background-color: var(--primary);
    border: none;
}
</style>