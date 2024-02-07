import { ServiceResponse } from "../domain/service-response"

class AjaxHelper <T>{
        private base_url:string = "/cemh-console-api/"

        constructor() {

       }

        async doGet(apiUrl:string, onError:(errorMessage:string, extraData:any) => any): Promise<T |  undefined> {

                const response = await fetch( this.base_url + apiUrl)
                if(!response.ok) {
                       return onError("Unhandled Error. Response Code: " + response.status, {statusCode: response.status})
          }

          const data = await response.text()
           var obj = new ServiceResponse<T>(JSON.parse(data))

           if(obj.getStatusCode() != 200) {
                  return onError(obj.getStatusMessage(), {statusCode: obj.getStatusCode))
           }

           return obj.getData();

       }

}

export {AjaxHelper}