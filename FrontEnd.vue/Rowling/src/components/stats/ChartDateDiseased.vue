<script setup>
import { ref, onMounted } from "vue";
import { HttpRequester } from './nets'; // Adjust the file path as necessary

const bearer = 'hi';
const locations = ref([
    {
        name: "LocationX",
        
    },
    {
        name: "LocationY",
        
    }
])
const selectedLocation = ref(locations.value[0]);

const dates = ref();
const percentages = ref();

async function fetchDatesDiseases() {
    const requester = new HttpRequester('http://127.0.0.1:8000/get-date-per-diseased-plants', bearer);
    const queryParams = {
        location: selectedLocation.value,
    };
    const requester_data = await requester.callApi(queryParams);
    dates.value = requester_data.dates;
    percentages.value = requester_data.percentages;
}

onMounted(async () => {
    await fetchDatesDiseases();
    chartData.value = setChartData();
    chartOptions.value = setChartOptions();
    
});


const chartData = ref();
const chartOptions = ref();

const setChartData = () => {
    const constantColorValue = 'rgba(164, 206, 149, 1)';
    const colorsArray = new Array(percentages.length).fill(constantColorValue);

    const constantBorderValue = 'rgb(139, 92, 246)';
    const bordersArray = new Array(percentages.length).fill(constantBorderValue);
    return {
        labels: dates.value,
        datasets: [
            {
                label: 'Percentage of diseased plants',
                data: percentages.value,
                backgroundColor: colorsArray,
                borderColor: bordersArray,
                borderWidth: 1
            }
        ]
    };
};
const setChartOptions = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--text-color');
    const textColorSecondary = documentStyle.getPropertyValue('--text-color-secondary');
    const surfaceBorder = documentStyle.getPropertyValue('--surface-border');

    return {
        plugins: {
            legend: {
                labels: {
                    color: textColor
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder
                }
            },
            y: {
                beginAtZero: true,
                ticks: {
                    color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder
                }
            }
        }
    };
}
</script>
<template>
    <el-row>
        <el-col :span="8" :xs="24" :sm="24" :md="24" :lg="8" :xl="8">
            <div class="grid-content ep-bg-purple">
                <p class="pre-date" style="margin:20px"> Location </p>
                <div class="card flex justify-content-center" style="margin:20px">
                    <CascadeSelect v-model="selectedLocation" :options="locations" optionLabel="name"
                        optionGroupLabel="name" :optionGroupChildren="['subLocations']" style="min-width: 14rem"
                        placeholder="Select a Location" />
                </div>
            </div>
        </el-col>
    </el-row>
    <el-row>
        <el-col :span="24">
            <div class="chart-parent-center">
                <div clas="grid-content ep-bg-purple chart-parent">
                    <div class="card flex justify-content-center chart-parent">
                        <Chart type="bar" :data="chartData" :options="chartOptions" />
                    </div>
                </div>
            </div>>

        </el-col>
    </el-row>

</template>

<style scoped>
.chart-parent {
    width: 500px;
    height: 500px;
    background-color: var(--primary);
}

.chart-parent-center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;

}
</style>