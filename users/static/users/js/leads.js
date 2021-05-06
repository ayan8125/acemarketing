$(document).ready( function () {
    $('#leads_table').DataTable();
} );


function pull_Date() {
    today_date = document.getElementById('t-date');
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           // Typical action to be performed when the document is ready:
           var responsedata = JSON.parse(this.response)
           today_date.innerHTML = responsedata.date
        }
    };
    xhttp.open("GET", '/user/give_date/', true);
    xhttp.send();

}



function serialize_Data(data) {
    const serailize_data = {
        labels: data.labels,
        datasets: [
            {
                label: data.label,
                data: data.points,
                backgroundColor: ['rgba(220,20,60,1)', 'rgb(0,191,255,1)'],
            }
        ]
    };

    return serailize_data
}

function make_request(url, result_to_dispatch_At_Id, result_to_dispatch_At_Id2) {
    var total_reach_element = document.getElementById('total-reach')
    var total_lead_element = document.getElementById('total-lead')
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           // Typical action to be performed when the document is ready:
           var responsedata = JSON.parse(this.response)
           var total_reach = responsedata.serach_engine_leads_reachs+responsedata.social_media_leads_reachs
           var total_leads = responsedata.serach_engine_leads_clicks+responsedata.social_media_leads_clicks
           total_reach_element.innerHTML = total_reach;
           total_lead_element.innerHTML = total_leads;
            const piedata1 = serialize_Data({
                lable: 'Search Engine and Socail Media Reachs',
                labels: ['Search Engine Reachs', 'Social Media Reachs'],
                points: [responsedata.serach_engine_leads_reachs, responsedata.social_media_leads_reachs],

            })
            drawChart('doughnut', result_to_dispatch_At_Id,piedata1, 'Reachs')

            const piedata2 = serialize_Data({
                lable: 'Search Engine and Socail Media Leads',
                labels: ['Search Engine Leads', 'Social Media leads'],
                points: [responsedata.serach_engine_leads_clicks, responsedata.social_media_leads_clicks],

            })
            drawChart('doughnut', result_to_dispatch_At_Id2,piedata2, 'Leads')
           

               
           }

        }

    xhttp.open("GET", url, true);
    xhttp.send();

}


function drawChart(type, chart_to_dipatch_at_id, data, title) {
    var ctx = document.getElementById(chart_to_dipatch_at_id).getContext('2d');
    var myChart = new Chart(ctx, {
    type: type,
    data: data,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                       font: {
                        size: 14
                    }
                }
            },
            title: {
                display: true,
                text: title
            }
        }
    },
});
}


function get_content(url, dispatch_id) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        // Typical action to be performed when the document is ready:
        document.getElementById(dispatch_id).innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();

}

pull_Date();
make_request('/user/get-social-and-engine-leads-reach-clicks/', 'leardsreachChart', 'leadsclicksChart');


