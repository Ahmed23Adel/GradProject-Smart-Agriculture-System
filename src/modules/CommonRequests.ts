import { HttpRequester } from '@/services/ApiCaller.ts';
import type { Ref, reactive } from 'vue'; // Import necessary types
 // Import necessary types

export async function fetchAllLocations(locations: Ref<any[]>, selectedLocation: Ref<any>) {
    const requester = new HttpRequester('get-diseased-locations');
    locations.value = [];
    await requester.callApi("GET").then(requester_data => {
        for (const loc of requester_data.locations) {
            locations.value.push({ name: loc });
        }
        // selectedLocation.value = locations.value[0];
        return locations.value[0].name;
    }).catch(error => {
        console.error("Error fetching locations:", error);
    });

}
