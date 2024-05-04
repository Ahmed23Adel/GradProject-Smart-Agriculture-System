import { HttpRequester } from '@/services/ApiCaller.ts';
import { ref } from 'vue';

export function fetchAllLocations(locations: ref<any[]>, selectedLocation: ref<any>) {
    const requester = new HttpRequester('get-diseased-locations');
    requester.callApi("GET").then(requester_data => {
        for (const loc of requester_data.locations) {
            locations.value.push({ name: loc });
        }
        selectedLocation.value = locations.value[0];
    }).catch(error => {
        console.error("Error fetching locations:", error);
    });
}
