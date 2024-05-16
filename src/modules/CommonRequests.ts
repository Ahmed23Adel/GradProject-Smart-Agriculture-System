import { HttpRequester } from '@/services/ApiCaller.ts';
import type { Ref, reactive } from 'vue'; // Import necessary types
 // Import necessary types

export function fetchAllLocations(locations: Ref<any[]>, selectedLocation: Ref<any>) {
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
