<script setup>
import { ref, watch, onMounted } from "vue";
import { HttpRequester } from '@/services/ApiCaller.ts';
import { fetchAllLocations } from '@/modules/CommonRequests.ts';
import { formatDate } from '@/modules/Basic.ts';


const locations = ref([])
const selectedLocation = ref();
const today = new Date();
const fromDate = ref(new Date(today.getFullYear(), 0, 1));
const toDate = ref(today);
const images = ref();
const isShowLoading = ref(true)
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


async function fetchLocationHistory(location, fromDate, toDate) {
    const requester = new HttpRequester('location-history');
    const queryParams = {
        location: selectedLocation.value.name,
        from_date: fromDate,
        to_date: toDate,
    };
    const requester_data = await requester.callApi('GET', queryParams);
    images.value = requester_data.allHistory;
}



onMounted(async () => {
    await fetchAllLocations(locations, selectedLocation);
    selectedLocation.value = locations.value[0];
    const formattedFromDate = formatDate(fromDate.value);
    const formattedToDate = formatDate(toDate.value);
    await fetchLocationHistory(location, formattedFromDate, formattedToDate);
    isShowLoading.value = false;
});

watch([selectedLocation, fromDate, toDate], async (newValues, oldValues) => {
    isShowLoading.value = true;
    const [newLocation, newFromDate, newToDate] = newValues;

    // Format the new dates
    const formattedFromDate = formatDate(newFromDate);
    const formattedToDate = formatDate(newToDate);

    // Call fetchLocationHistory with the new values
    await fetchLocationHistory(newLocation, formattedFromDate, formattedToDate);
    isShowLoading.value = false;
});
</script>


<template>
    <div class="row">
        <div class="col-12">
            <div clas="grid-content ep-bg-purple">
                <!-- <h2 class="sub-header-gen-stats" style="color:white">History of certain location:</h2> -->
                <h1 class="h3">History of certain location:</h1>
            </div>
        </div>
    </div>

    <div class="selectors">
        <div class="row">
            <div class="col-4">
                <div class="grid-content ep-bg-purple">
                    <p class="pre-date" style="margin:20px"> Location </p>
                    <div class="card flex justify-content-center" style="margin:20px">
                        <CascadeSelect v-model="selectedLocation" :options="locations" optionLabel="name"
                            optionGroupLabel="name" :optionGroupChildren="['subLocations']" style="min-width: 14rem"
                            placeholder="Select a Location" />
                    </div>
                </div>
            </div>

            <div class="col-4">
                <div class="grid-content ep-bg-purple">
                    <p class="pre-date" style="margin:20px"> From: </p>
                    <div class="card flex justify-content-center" style="margin:20px">
                        <Calendar v-model="fromDate" />

                    </div>
                </div>
            </div>

            <div class="col-4">
                <div class="grid-content ep-bg-purple">
                    <p class="pre-date" style="margin:20px"> To: </p>
                    <div class="card flex justify-content-center" style="margin:20px">
                        <Calendar v-model="toDate" />
                    </div>
                </div>
            </div>

        </div>
        <div class="row justify-content-center" v-if="isShowLoading">
            <div class="col-12 text-center">
                <ProgressSpinner />
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <div class="grid-content ep-bg-purple graph-image-parent">
                    <div class="card images-parent">
                        <Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5"
                            containerStyle="max-width: 640px">
                            <template #item="slotProps">
                                <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt"
                                    class="fixed-size-image" @change="onChangeImage" crossorigin="anonymous" />
                            </template>
                            <template #thumbnail="slotProps">
                                <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt"
                                    class="fixed-size-thumbnail" crossorigin="anonymous" />
                            </template>
                            <template #caption="slotProps">
                                <div class="text-xl mb-2 font-bold">{{ slotProps.item.title }}</div>
                                <p class="text-white">{{ slotProps.item.alt }}</p>
                            </template>
                        </Galleria>
                    </div>
                </div>

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

.images-parent {
    background-color: var(--primary);
    border: none;
}

.fixed-size-image {
    width: 600px;
    height: 450px;
    object-fit: cover; /* or "contain" depending on the desired effect */
    display: block;
}

.fixed-size-thumbnail {
    width: 80px;
    height: 80px;
    object-fit: cover; /* or "contain" */
    display: block;
}

</style>