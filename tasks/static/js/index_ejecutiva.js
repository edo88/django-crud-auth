    let dataTableSolicitudes;

    let dataTableSolicitudesIsInitialized = false;

    const tableBody_solicitudes = document.querySelector("#tableBody_solicitudes");


const dataTableSolicitudesOptions={
    columnDefs: [
    { className: "centered", targets: [0, 1] },
    { orderable: false, targets: [1] },
    { searchable: true, targets: [1] }
    ],
    pageLength: 5,
    destroy: true
};  


const initDateTableSolicitudes = async () => {
    if(dataTableSolicitudesIsInitialized){
        dataTableSolicitudes.destroy();
    }
    
    await listSolicitudes();
    
    dataTableSolicitudes=$('#datatable_solicitudes').DataTable(dataTableSolicitudesOptions);
    
    dataTableSolicitudesIsInitialized = true;
    
    };

const listSolicitudes = async () =>{
    try{
        const response = await fetch("http://127.0.0.1:8000/list_solicitudes");
        
        const data = await response.json();

        let content = ``;
        data.solicitudes.forEach((solicitud, index)=>{
        content+=`
            <tr>
                <td>${index + 1}</td>
                <td>${solicitud.comentario}</td>
                <td>${solicitud.user}</td>
                <td>${solicitud.requerimiento}</td>

            </tr>
        `;
        });
        tableBody_solicitudes.innerHTML = content;
        console.log(data.solicitudes);
    }catch(ex){
        alert(ex);
    }
};

window.addEventListener("load", async () =>{
    await initDateTableSolicitudes();

});