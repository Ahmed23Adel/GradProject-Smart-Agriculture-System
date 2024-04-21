<script setup>
import { ref, watch, onMounted } from "vue";
import GraphOfImages from "./GraphOfImages.vue"
import { HttpRequester } from './nets'; // Adjust the file path as necessary
const bearer = 'hi';


const locations = ref([])
const selectedLocation = ref();
const locs = ref()
async function fetchAllLocs() {

const requester = new HttpRequester('http://127.0.0.1:8000/get-diseased-locations', bearer);
const requester_data = await requester.callApi();
locs.value = requester_data.locations;
console.log(locs.value);
for (const loc of locs.value) {
    locations.value.push({ name: loc });
}
selectedLocation.value = locations.value[0];

}

// onMounted(async () => {
   

// });

const today = new Date(); // Create a new Date object for today's date
const fromDate = ref(today);
const toDate = ref(today);


async function fetchLocationHistory(location, fromDate, toDate) {
    const requester = new HttpRequester('http://127.0.0.1:8000/location-history', bearer);
    const queryParams = {
        location: selectedLocation.value.name,
        from_date: fromDate,
        to_date: toDate,
    };
    const requester_data = await requester.callApi(queryParams);
    images.value = requester_data.allHistory;
}

function formatDate(date) {
    const month = date.getMonth() + 1; // Months are 0-based, so add 1
    const day = date.getDate();
    const year = date.getFullYear();
    // Pad month and  with leading zeros if necessary
    const paddedMonth = month.toString().padStart(2, '0');
    const paddedDay = day.toString().padStart(2, '0');
    // Return the formatted date as a string
    return `${paddedMonth}/${paddedDay}/${year}`;
}

const images = ref();
const responsiveOptions = ref([
    {
        breakpoint: '1300px',
        numVisible: 4
    },
    {
        breakpoint: '575px',
        numVisible: 1
    }
]);

onMounted(async () => {
    await fetchAllLocs();
    const formattedFromDate = formatDate(fromDate.value);
    const formattedToDate = formatDate(toDate.value);
    fetchLocationHistory(location, formattedFromDate, formattedToDate);
});

watch([selectedLocation, fromDate, toDate], (newValues, oldValues) => {
    const [newLocation, newFromDate, newToDate] = newValues;

    // Format the new dates
    const formattedFromDate = formatDate(newFromDate);
    const formattedToDate = formatDate(newToDate);

    // Call fetchLocationHistory with the new values
    fetchLocationHistory(newLocation, formattedFromDate, formattedToDate);
});
</script>


<template>
    <el-row>
        <el-col :span="22">
            <div clas="grid-content ep-bg-purple">
                <!-- <h2 class="sub-header-gen-stats" style="color:white">History of certain location:</h2> -->
                <h1 class="h3">History of certain location:</h1>
            </div>
        </el-col>
    </el-row>

    <div class="selectors">
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
                    <p class="pre-date" style="margin:20px"> To: </p>
                    <div class="card flex justify-content-center" style="margin:20px">
                        <Calendar v-model="toDate" />
                    </div>
                </div>
            </el-col>

        </el-row>

        <el-row>
            <el-col :span="24">
                <div class="grid-content ep-bg-purple graph-image-parent">
                    <div class="card">
                        <Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" containerStyle="max-width: 640px">
                            <template #item="slotProps">
                                <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
                            </template>
                            <template #thumbnail="slotProps">
                                <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block" />
                            </template>
                            <template #caption="slotProps">
                                <div class="text-xl mb-2 font-bold">{{ slotProps.item.title }}</div>
                                <p class="text-white">{{ slotProps.item.alt }}</p>
                            </template>
                        </Galleria>
                    </div>
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

.pre-date{
    font-size: 28px;
}
</style>