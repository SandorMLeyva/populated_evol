Vue.component('woman_death', {
    template: '<canvas id="w_d"></canvas>'
});

Vue.component('man_death', {
    template: '<canvas id="m_d"></canvas>'
});
Vue.component('death_by_age', {
    template: '<canvas id="d_b_a"></canvas>'
});
Vue.component('woman_born', {
    template: '<canvas id="w_b"></canvas>'
});
Vue.component('man_born', {
    template: '<canvas id="m_b"></canvas>'
});
Vue.component('death_by_age_all', {
    template: '<canvas id="d_b_a_a"></canvas>'
});
Vue.component('man_vs_woman', {
    template: '<canvas id="m_vs_w"></canvas>'
})
;Vue.component('widow', {
    template: '<canvas id="widow"></canvas>'
});
Vue.component('lovers', {
    template: '<canvas id="lovers"></canvas>'
});
Vue.component('broken_partners', {
    template: '<canvas id="b_p"></canvas>'
});
Vue.component('timeout', {
    template: '<canvas id="time_out"></canvas>'
});
Vue.component('max_born', {
    template: '<canvas id="mm_b"></canvas>'
});
Vue.component('max_death', {
    template: '<canvas id="mm_d"></canvas>'
});

function graphic(x,y, id, type, fill = false, showLine = true) {
    var ctx = document.getElementById(id).getContext('2d');
    new Chart(ctx, {
        type: type,
        data: {
            // x
            labels: x,
            // y
            datasets: [{
                data: y,
                borderWidth: 1,
                fill: fill,
                pointRadius: 8,
                pointHoverRadius: 5,
                showLine: showLine,// no line shown
                backgroundColor: type== 'line' ? ['rgba(54, 162, 235, 0.2)']: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(2, 78, 32, 0.2)',
                'rgba(154, 112, 35, 0.2)',
                'rgba(25, 106, 86, 0.2)',
                'rgba(85, 19, 192, 0.2)',
                'rgba(15, 102, 255, 0.2)',
                'rgba(20, 200, 62, 0.2)',
                'rgba(154, 112, 35, 0.2)',
                'rgba(25, 106, 86, 0.2)',
                'rgba(85, 19, 192, 0.2)',
                'rgba(15, 102, 255, 0.2)',
                'rgba(20, 200, 62, 0.2)'
                 ],
                borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                 'rgba(2, 78, 32, 1)',
                'rgba(154, 112, 35, 1)',
                'rgba(25, 106, 86, 1)',
                'rgba(85, 19, 192, 1)',
                'rgba(15, 102, 255, 1)',
                'rgba(20, 200, 62, 1)',
                'rgba(154, 112, 35, 1)',
                'rgba(25, 106, 86, 1)',
                'rgba(85, 19, 192, 1)',
                'rgba(15, 102, 255, 1)',
                'rgba(20, 200, 62, 1)'

            ],
            borderWidth: 1
            }],
            options: {
                responsive: true,
                title:{
                    display:true,
                    text:'Chart.js Line Chart'
                },
                tooltips: {
                    mode: 'index',
                    intersect: false,
                },
                hover: {
                    mode: 'nearest',
                    intersect: true
                },
                scales: {
                    xAxes: [{
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: 'Month'
                        }
                    }],
                    yAxes: [{
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: 'Value'
                        }
                    }]
                }
            }


        },
    });
}

var app;
app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        year: 1,
        final: 0,
        woman: 0,
        man: 0,
        months: 0
    },
    mounted: function () {
        this.summary();
        this.death_woman();
        this.death_man();
        this.death_by_age(this.year);
        this.borns_man();
        this.borns_woman();
        this.death_by_age_all();
        this.man_vs_woman();
        this.widow();
        this.lovers();
        this.broken_partners();
        this.timeout(this.year);
        this.max_born();
        this.max_death();

    },
    methods: {
        summary: () =>{
             axios.get('/summary').then(
                response => {
                    app.final = response.data.final;
                    app.woman = response.data.woman;
                    app.man = response.data.man;
                    app.months = response.data.months;
                }
            );
        },
        death_woman: () => {
            axios.get('/death/female').then(
                response => {
                    graphic(response.data.len, response.data.number_d, 'w_d', 'bar')
                }
            );

        },
        death_man: () => {
            axios.get('/death/male').then(
                response => {
                    graphic(response.data.len, response.data.number_d, 'm_d', 'bar')
                }
            );

        },
        borns_man: () => {
            axios.get('/born/male').then(
                response => {
                    graphic(response.data.len, response.data.number_d, 'm_b', 'line', false, false)
                }
            );
        },
        borns_woman: () => {
            axios.get('/born/female').then(
                response => {
                    graphic(response.data.len, response.data.number_d, 'w_b', 'line', false, false)
                }
            );
        },
        death_by_age: (year) => {
            axios.get('/deathbyage/' + year).then(
                response => {
                    graphic(response.data.x, response.data.data, 'd_b_a', 'line')
                }
            );
        },
        death_by_age_all: () => {
            axios.get('/deathbyage/all').then(
                response => {
                    graphic(response.data.x, response.data.data, 'd_b_a_a', 'line')
                }
            );
        },
        man_vs_woman: () => {//nacidos
            axios.get('/manvswoman').then(
                response => {
                    graphic(['Hombres', 'Mujeres'], [response.data.man, response.data.woman], 'm_vs_w', 'bar')
                }
            );
        },
        widow: () => {
              axios.get('/widow').then(
                response => {
                    graphic(response.data.x, response.data.data, 'widow', 'line')
                }
            );
        },
        lovers: () => {
              axios.get('/lovers').then(
                response => {
                    graphic(response.data.x, response.data.data, 'lovers', 'line')
                }
            );
        },
        broken_partners: () => {
              axios.get('/brokenpartners').then(
                response => {
                    graphic(response.data.x, response.data.data, 'b_p', 'line')
                }
            );
        },
        timeout: (year) => {
            axios.get('/timeout/' + year).then(
                response => {
                    graphic(response.data.x, response.data.data, 'time_out', 'line')
                }
            );
        },
        max_death: () => {
              axios.get('/maxdeath').then(
                response => {
                    graphic(response.data.x, response.data.data, 'mm_d', 'line')
                }
            );
        },
        max_born: () => {
              axios.get('/maxborn').then(
                response => {
                    graphic(response.data.x, response.data.data, 'mm_b', 'line')
                }
            );
        },
        next_year: () => {
            app.year += 1;
            app.death_by_age(app.year)
            app.timeout(app.year);
        },
        prev_year: () => {
            if(app.year == 1){
                alert('Estas en el primer año de la simulacion')
            }
            else
                app.year -= 1
            app.death_by_age(app.year)
            app.timeout(app.year);

        }

    }
});


