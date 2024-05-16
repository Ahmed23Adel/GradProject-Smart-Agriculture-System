import { HttpRequester } from '@/services/ApiCaller.ts';
import { ref } from 'vue';

export function fetchAllLocations(locations: ref<any[]>, selectedLocation: ref<any>) {
    const requester = new HttpRequester('get-diseased-locations');
    console.log("locations.value", locations.value)
    locations.value = [];
    console.log("locations.value", locations.value)
    requester.callApi("GET").then(requester_data => {
        for (const loc of requester_data.locations) {
            locations.value.push({ name: loc });
            console.log("push")
        }
        // selectedLocation.value = locations.value[0];
        return locations.value[0].name;
    }).catch(error => {
        console.error("Error fetching locations:", error);
    });

}
