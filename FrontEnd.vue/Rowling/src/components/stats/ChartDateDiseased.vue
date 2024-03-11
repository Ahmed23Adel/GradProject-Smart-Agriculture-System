<script setup>
import { ref, onMounted } from "vue";


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


onMounted(() => {
    chartData.value = setChartData();
    chartOptions.value = setChartOptions();
});

const chartData = ref();
const chartOptions = ref();

const setChartData = () => {
    return {
        labels: ['22-4-2024', '23-4-2024', '22-4-2024', '24-4-2024'],
        datasets: [
            {
                label: 'Percentage of diseased plants',
                data: [83, 75, 65, 50],
                backgroundColor: ['rgba(164, 206, 149, 1)', 'rgba(164, 206, 149, 1)', 'rgba(164, 206, 149, 1)', 'rgba(164, 206, 149, 1)'],
                borderColor: ['rgb(164, 206, 149)', 'rgb(6, 182, 212)', 'rgb(107, 114, 128)', 'rgb(139, 92, 246)'],
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
                    <CascadeSelect v-model="selectedLocation" :options="locations" optionLabel="cname"
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