import axios from 'axios';

export class HttpRequester{
    private endpoint;
    private bearer;

    constructor(endpoint: string, bearer: string) {
        this.endpoint = endpoint;
        this.bearer = bearer;
    } 

    public async callApi(queryParams?: Record<string, any>): Promise<any> {
        try {
            // Construct the URL with query parameters if provided
            const url = new URL(this.endpoint);
            if (queryParams) {
                // Append query parameters to the URL
                for (const [key, value] of Object.entries(queryParams)) {
                    url.searchParams.append(key, value.toString());
                }
            }
            // Make a GET request to the constructed URL with the Bearer token in the headers
            const response = await axios.get(url.toString(), {
                headers: {
                    Authorization: `Bearer ${this.bearer}`,
                },
            });

            // Check if the response has data and success status
            if (response.data && response.data.success) {
                // Return the response data
                return response.data.data;
            } else {
                console.error('API response did not indicate success');
            }
        } catch (error) {
            console.error('Error calling API:', error);
        }
    }
}