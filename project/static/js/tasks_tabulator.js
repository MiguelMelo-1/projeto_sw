import Tabulator from "tabulator-tables";

// let table = new Tabulator("#tabela-tasks", {
//     ajaxURL: "./dados_cabecalho_trabalhos",
//     // ajaxFiltering: true,
//     // ajaxSorting: true,
//     printAsHtml: true,
//     printStyled: true,
//     pagination: "local",
//     paginationSize: 10,
//     paginationSizeSelector: [10, 20, 30, 40],
//     layout: "fitColumns",
//     responsiveLayout: "collapse",
//     placeholder: "Nenhum trabalho encontrado",
//     columns: [
//         {
//             formatter: "responsiveCollapse",
//             width: 40,
//             minWidth: 30,
//             hozAlign: "center",
//             resizable: false,
//             headerSort: false,
//         },

//         // For HTML table
//         {
//             title: "Tipo de Trabalho",
//             minWidth: 200,
//             field: "tipo_trabalho",
//             // hozAlign: "right",
//             vertAlign: "middle",
//             print: false,
//             download: false,
//         },
//         {
//             title: "Ações",
//             minWidth: 200,
//             field: "actions",
//             responsive: 1,
//             // hozAlign: "right",
//             vertAlign: "middle",
//             print: false,
//             download: false,
//             formatter(cell, formatterParams) {
//                 return `<div class="flex lg:justify-center items-center">
//                     <a class="edit flex items-center mr-3" href="./ver-orcamento/${cell.getData().id}">
//                         <i class="w-4 h-4 mr-1 fa fa-eye fa-xl" style="color:#FF7A13;"></i>
//                     </a>`
//             },
//         },
//         // {
//             // title: "Estado",
//             // minWidth: 200,
//             // responsive: 0,
//             // field: "estado",
//             // vertAlign: "middle",
//             // print: false,
//             // download: false,
//             // formatter(cell, formatterParams) {
//             //     switch (cell.getData().estado){

//             //         case 'pendente':

//             //             return `<div class="flex lg:justify-center items-center">
//             //                 <i class="w-4 h-4 mr-1 fa fa-circle-check fa-xl" style="color:#eed202;"> Pendente</i>
//             //                 </div>`;
//             //                 break;

//             //         case 'aprovado':
//             //             return `<div class="flex lg:justify-center items-center">
//             //                 <i class="w-4 h-4 mr-1 fa fa-circle-check fa-xl" style="color:green;"> Aprovado</i>
//             //                 </div>`;
//             //                 break;

//             //         case 'recusado':
//             //             return `<div class="flex lg:justify-center items-center">
//             //                 <i class="w-4 h-4 mr-1 fa fa-circle-xmark fa-xl" style="color:red;"> Recusado</i>
//             //                 </div>`;
//             //                 break;
//             //         default:
//             //             return `ok`;

//             //     }
//             // },
//         // },
//         // {
//             // title: "N.º de Orçamento",
//             // minWidth: 200,
//             // responsive: 0,
//             // field: "id",
//             // vertAlign: "middle",
//             // print: false,
//             // download: false,
//             // formatter(cell, formatterParams) {
//             //     return `<div>
//             //         <div class="font-medium whitespace-nowrap">${
//             //             cell.getData().name
//             //         }</div>
//             //         <div class="text-slate-500 text-xs whitespace-nowrap">${
//             //             cell.getData().category
//             //         }</div>
//             //     </div>`;
//             // },
//         // },
//         // {
//         //     title: "IMAGES",
//         //     minWidth: 200,
//         //     field: "images",
//         //     hozAlign: "center",
//         //     vertAlign: "middle",
//         //     print: false,
//         //     download: false,
//         //     formatter(cell, formatterParams) {
//         //         return `<div class="flex lg:justify-center">
//         //             <div class="intro-x w-10 h-10 image-fit">
//         //                 <img alt="Midone - HTML Admin Template" class="rounded-full" src="/dist/images/${
//         //                     cell.getData().images[0]
//         //                 }">
//         //             </div>
//         //             <div class="intro-x w-10 h-10 image-fit -ml-5">
//         //                 <img alt="Midone - HTML Admin Template" class="rounded-full" src="/dist/images/${
//         //                     cell.getData().images[1]
//         //                 }">
//         //             </div>
//         //             <div class="intro-x w-10 h-10 image-fit -ml-5">
//         //                 <img alt="Midone - HTML Admin Template" class="rounded-full" src="/dist/images/${
//         //                     cell.getData().images[2]
//         //                 }">
//         //             </div>
//         //         </div>`;
//         //     },
//         // },
//         // {
//         //     title: "Cliente",
//         //     minWidth: 200,
//         //     field: "nome",
//         //     // hozAlign: "right",
//         //     vertAlign: "middle",
//         //     print: false,
//         //     download: false,
//         //     formatter(cell, formatterParams) {
//         //         return `<div>
//         //                 <div class="font-medium whitespace-nowrap">${
//         //                     cell.getData().nome
//         //                 }</div>
//         //                 <div class="text-slate-500 text-xs whitespace-nowrap">${
//         //                     cell.getData().tlm
//         //                 }</div>
//         //             </div>`;
//         //     },
//         // },
//         // {
//         //     title: "Local",
//         //     minWidth: 200,
//         //     field: "morada",
//         //     // hozAlign: "right",
//         //     vertAlign: "middle",
//         //     print: false,
//         //     download: false,
//         // },
//         //     {
//         //     title: "Ações",
//         //     minWidth: 200,
//         //     field: "actions",
//         //     responsive: 1,
//         //     hozAlign: "center",
//         //     vertAlign: "middle",
//         //     print: false,
//         //     download: false,
//         //     formatter(cell, formatterParams) {
//         //         let a =
//         //             $(`<div class="flex lg:justify-center items-center">
//         //             <a class="edit flex items-center mr-3" href="/trabalho-pendente/${cell.getData().status}">
//         //                 <i class="w-4 h-4 mr-1 fa fa-eye"></i>
//         //             </a>
//         //             <a class="delete flex items-center text-danger" href="javascript:;">
//         //                 <i icon-name="trash-2" class="w-4 h-4 mr-1"></i> Delete
//         //             </a>
//         //         </div>`);
//         //         $(a)
//         //             .find(".edit")
//         //             .on("click", function () {
//         //                 alert("EDIT");
//         //             });

//         //         $(a)
//         //             .find(".delete")
//         //             .on("click", function () {
//         //                 alert("DELETE");
//         //             });

//         //         return a[0];
//         //     },
//         // },

//         // For print format
//         // {
//         //     title: "PRODUCT NAME",
//         //     field: "name",
//         //     visible: false,
//         //     print: true,
//         //     download: true,
//         // },
//         // {
//         //     title: "CATEGORY",
//         //     field: "category",
//         //     visible: false,
//         //     print: true,
//         //     download: true,
//         // },
//         // {
//         //     title: "REMAINING STOCK",
//         //     field: "remaining_stock",
//         //     visible: false,
//         //     print: true,
//         //     download: true,
//         // },
//         // {
//         //     title: "STATUS",
//         //     field: "status",
//         //     visible: false,
//         //     print: true,
//         //     download: true,
//         //     formatterPrint(cell) {
//         //         return cell.getValue() ? "Active" : "Inactive";
//         //     },
//         // },
//         // {
//         //     title: "IMAGE 1",
//         //     field: "images",
//         //     visible: false,
//         //     print: true,
//         //     download: true,
//         //     formatterPrint(cell) {
//         //         return cell.getValue()[0];
//         //     },
//         // },
//         // {
//         //     title: "IMAGE 2",
//         //     field: "images",
//         //     visible: false,
//         //     print: true,
//         //     download: true,
//         //     formatterPrint(cell) {
//         //         return cell.getValue()[1];
//         //     },
//         // },
//         // {
//         //     title: "IMAGE 3",
//         //     field: "images",
//         //     visible: false,
//         //     print: true,
//         //     download: true,
//         //     formatterPrint(cell) {
//         //         return cell.getValue()[2];
//         //     },
//         // },
//     ],
//     renderComplete() {
//         createIcons({
//             icons,
//             "stroke-width": 1.5,
//             nameAttr: "data-lucide",
//         });
//     },
// });

//define data array
var tabledata = [
  {
    id: 1,
    name: "Oli Bob",
    progress: 12,
    gender: "male",
    rating: 1,
    col: "red",
    dob: "19/02/1984",
    car: 1,
  },
  {
    id: 2,
    name: "Mary May",
    progress: 1,
    gender: "female",
    rating: 2,
    col: "blue",
    dob: "14/05/1982",
    car: true,
  },
  {
    id: 3,
    name: "Christine Lobowski",
    progress: 42,
    gender: "female",
    rating: 0,
    col: "green",
    dob: "22/05/1982",
    car: "true",
  },
  {
    id: 4,
    name: "Brendon Philips",
    progress: 100,
    gender: "male",
    rating: 1,
    col: "orange",
    dob: "01/08/1980",
  },
  {
    id: 5,
    name: "Margret Marmajuke",
    progress: 16,
    gender: "female",
    rating: 5,
    col: "yellow",
    dob: "31/01/1999",
  },
  {
    id: 6,
    name: "Frank Harbours",
    progress: 38,
    gender: "male",
    rating: 4,
    col: "red",
    dob: "12/05/1966",
    car: 1,
  },
];

//initialize table
var table = new Tabulator("#example-table", {
  data: tabledata, //load row data from array
  layout: "fitColumns", //fit columns to width of table
  responsiveLayout: "hide", //hide columns that don't fit on the table
  addRowPos: "top", //when adding a new row, add it to the top of the table
  history: true, //allow undo and redo actions on the table
  pagination: "local", //paginate the data
  paginationSize: 7, //allow 7 rows per page of data
  paginationCounter: "rows", //display count of paginated rows in footer
  movableColumns: true, //allow column order to be changed
  initialSort: [
    //set the initial sort order of the data
    { column: "name", dir: "asc" },
  ],
  columnDefaults: {
    tooltip: true, //show tool tips on cells
  },
  columns: [
    //define the table columns
    { title: "Name", field: "name", editor: "input" },
    {
      title: "Task Progress",
      field: "progress",
      hozAlign: "left",
      formatter: "progress",
      editor: true,
    },
    {
      title: "Gender",
      field: "gender",
      width: 95,
      editor: "select",
      editorParams: { values: ["male", "female"] },
    },
    {
      title: "Rating",
      field: "rating",
      formatter: "star",
      hozAlign: "center",
      width: 100,
      editor: true,
    },
    { title: "Color", field: "col", width: 130, editor: "input" },
    {
      title: "Date Of Birth",
      field: "dob",
      width: 130,
      sorter: "date",
      hozAlign: "center",
    },
    {
      title: "Driver",
      field: "car",
      width: 90,
      hozAlign: "center",
      formatter: "tickCross",
      sorter: "boolean",
      editor: true,
    },
  ],
});
