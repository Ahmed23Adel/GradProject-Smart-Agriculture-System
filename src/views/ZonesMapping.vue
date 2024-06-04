<script setup>
import Sidebar from "../components/Sidebar.vue";
import { HttpRequester } from '@/services/ApiCaller.ts';
import { ref, onMounted, watch } from "vue";
import { findCoordinates, openGoogleMapsWithLatLong } from '@/modules/Basic.ts';

const grid = ref([])
const hoveredZone = ref (null)
const calculatedCoordinates = ref({})
const zoneNameSearch = ref("")
const minLat = 40.0;
const maxLat = 40.1;
const minLong = 50.0;
const maxLong = 50.1;
const zoneSize = 500 //m;
const maxZones = 1000;
function generateGrid() {
    
    
    // Calculate the maximum number of zones allowed
    
    
    // Calculate the number of zones needed to achieve approximately 200 zones
    
    const horizontalZones = Math.ceil((maxLong - minLong) * 111139 / zoneSize);
    const verticalZones = Math.ceil((maxLat - minLat) * 111139 / zoneSize);
    console.log(zoneSize, horizontalZones, verticalZones)
    let counter = 0;
    for (let i = 0; i < verticalZones; i++) {
        const row = [];
        for (let j = 0; j < horizontalZones; j++) {
            const zoneName = `Zone_${counter}. Longitude: ${minLong + i*zoneSize/111139} Latitude: ${minLat + i*zoneSize/111139}`;
            row.push({ name: zoneName });
            counter += 1;
        }
        grid.value.push(row);
    }
    // console.log("grid", grid.valu)
    return grid;
}
function showZoneName(zone) {
    hoveredZone.value = zone;
}

function hideZoneName() {
    // console.log("hideZoneName", zone)

    hoveredZone.value = null;
}



function openGoogleMaps(zone) {
    console.log("zone", zone)
    // Extracting longitude and latitude from the zone string
    const parts = zone.name.split('. ');
    const longitude = parseFloat(parts[1].split(' ')[1]);
    const latitude = parseFloat(parts[1].split(' ')[1]);

    // Constructing the Google Maps link
    const googleMapsLink = `https://www.google.com/maps?q=${latitude},${longitude}`;
    
    // Opening the link in a new tab
    window.open(googleMapsLink, '_blank');
}

function openGoogleMapsWithLatLongLocal() {
    openGoogleMapsWithLatLong(calculatedCoordinates.value)
}



onMounted(async () => {
    await generateGrid();
});

watch(zoneNameSearch, async (newzoneNameSearch, oldzoneNameSearch) => {
    findCoordinates(maxLong, minLong, maxLat, minLat, zoneSize, zoneNameSearch.value, calculatedCoordinates)
});

</script>
<template>
    <div class="page-container">
        <Sidebar class="sidebar" :selected="6" />
        <div class="main-container" style="margin-top:60px">
            <div class="zone-input row">
                <div class="col-3">
                    <FloatLabel>
                        <InputText id="zonename" v-model="zoneNameSearch" />
                        <label for="zonename">Zone name</label>
                    </FloatLabel>
                </div>
                
                <div class="col-3" style="margin-top: 10px;">
                    <div v-if="calculatedCoordinates">Longitude: {{ calculatedCoordinates.long }}, Latitude: {{ calculatedCoordinates.lat }}</div>
                </div>
                <div class="col-3">
                    <div v-if="calculatedCoordinates">
                        <Button label="Go to Google Maps" @click="openGoogleMapsWithLatLongLocal"/>
                    </div>
                </div>
            </div>
            <div id="app" style="position: relative;">
                <div v-for="(row, rowIndex) in grid" :key="rowIndex" class="grid-row">
                    <div v-for="(zone, zoneIndex) in row" :key="zoneIndex" class="zone" 
                        :style="{ left: zoneIndex * 55 + 'px', top: (grid.length - 1 - rowIndex) * 55 + 'px' }"
                        @mouseover="showZoneName(zone)"
                        @mouseout="hideZoneName"
                        @click="openGoogleMaps(zone)">
                        <div class="zone-name" v-if="hoveredZone === zone">{{ zone.name }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style lang="scss" scoped>
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

.grid-row {
    display: flex;
}

.zone {
    width: 50px;
    height: 50px;
    border: 1px solid black;
    display: flex;
    justify-content: center;
    align-items: center;
}

.zone:hover .zone-name {
    display: block;
}

.zone-name {
    display: none;
    position: absolute;
    background-color: white;
    padding: 5px;
    border: 1px solid black;
    z-index: 1;
}
.zone-input {
    margin-top: 20px;
    margin-bottom: 30px;
}

.zone-input input {
    margin-right: 10px;
}
</style>