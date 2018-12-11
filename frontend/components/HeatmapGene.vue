<template>
    <div class="heatmap-gene" v-if="series.length">
        <p class="heatmap-gene-title">{{ gene }}</p>
        <apexchart type=heatmap :height="height" :options="chartOptions" :series="series" />
    </div>
</template>

<script>
    export default {
        name: 'heatmap-gene',
        props: ['gene'],
        data () {
            return {
                chartOptions: {
                    legend: {
                        show: false
                    },
                    chart: {
                        // width: '500',
                        toolbar: {
                            show: false
                        },
                        animations: {
                            // enabled: true,
                            enabled: false,
                            easing: 'linear',
                            speed: 20,
                            animateGradually: {
                                enabled: false,
                            },
                            dynamicAnimation: {
                                enabled: false,
                                speed: 10
                            }
                        }
                    },
                    grid: {
                      margin: {
                        top: 0,
                        bottom: 0
                      }
                    },
                    dataLabels: {
                        enabled: false,
                    },
                    xaxis: {
                        labels: {
                            show: false,
                        },
                        axisTicks: {
                            show: false
                        },
                        axisBorder: {
                            show: false
                        }
                    },
                    yaxis: {
                        labels: {
                            minWidth: 80,
                        },
                    },
                    tooltip: {
                        enabled: true,
                        y: {
                            formatter: (val) => {
                                return ''
                            }
                        }
                    },
                    plotOptions: {
                        heatmap: {
                            enableShades: false,
                            // shadeIntensity: 0.5,
                            colorScale: {
                                ranges: [
                                    {
                                        from: 0,
                                        to: 0.1,
                                        color: '#FFFFFF'
                                    },
                                    {
                                        from: 1,
                                        to: 1,
                                        color: '#00004d'
                                    },
                                    {
                                        from: 2,
                                        to: 2,
                                        color: '#000066'
                                    },
                                    {
                                        from: 3,
                                        to: 3,
                                        color: '#000080'
                                    },
                                    {
                                        from: 4,
                                        to: 4,
                                        color: '#4d88ff'
                                    },
                                    {
                                        from: 5,
                                        to: 5,
                                        color: '#80aaff'
                                    },
                                    {
                                        from: 6,
                                        to: 6,
                                        color: '#b3ccff'
                                    },
                                    {
                                        from: 7,
                                        to: 7,
                                        color: '#ccccff'
                                    },
                                    {
                                        from: 8,
                                        to: 8,
                                        color: '#E8E8E8'
                                    },
                                    {
                                        from: 9,
                                        to: 9,
                                        color: '#ffb3b3'
                                    },
                                    {
                                        from: 10,
                                        to: 10,
                                        color: '#ff8080'
                                    },
                                    {
                                        from: 11,
                                        to: 11,
                                        color: '#ff6666'
                                    },
                                    {
                                        from: 12,
                                        to: 12,
                                        color: '#ff4d4d'
                                    },
                                    {
                                        from: 13,
                                        to: 13,
                                        color: '#e60000'
                                    },
                                    {
                                        from: 14,
                                        to: 14,
                                        color: '#990000'
                                    },
                                    {
                                        from: 100,
                                        to: 100,
                                        color: '#003366'
                                    },
                                    {
                                        from: -100,
                                        to: -100,
                                        color: '#b4b4b4'
                                    }
                                ]
                            }
                        }
                    },
                }
            }
        },
        computed: {
            height () {
                const series = this.series.length;
                const calcHeights = {
                    7: 110,
                    6: 100,
                    5: 90,
                    4: 80,
                    3: 72,
                    2: 62,
                    1: 54
                };
                return calcHeights[series]
            },
            series () {
                let dataTypes = [
                    ['phospho', 'Phospho'],
                    ['protein', 'Protein'],
                    ['rna', 'mRNA'],
                    ['cnv_baf', 'CNV (baf)'],
                    ['cnv_lr', 'CNV (lr)'],
                    ['methylation', 'Methy'],
                    ['mutation', 'Mut']
                ];
                let allData = [];
                dataTypes.forEach((dataType) => {
                    let data = this.$store.state[dataType[0]][this.gene];
                    if (data) {
                        allData.push(
                            {
                                name: dataType[1],
                                data: convertToArrayOfObjects(data)
                            }
                        )
                    }
                });
                return allData;
            }
        },
    }

    function convertToArrayOfObjects (obj) {
        if (!obj) {
        }
        let arrayOfObjects = [];
        Object.keys(obj).forEach((k) => {
            arrayOfObjects.push(
                {x: k, y: obj[k]}
            )
        });
        return arrayOfObjects;
    }

</script>

<style scoped>
    .heatmap-gene {
        position: relative;
        min-height: 80px;
    }

    .heatmap-gene-title {
        padding: 0;
        margin-bottom: -30px;
        margin-top: -20px;
        font-weight: bold;
        font-size: small;
    }

    /*.rotate {*/
      /*!* FF3.5+ *!*/
      /*-moz-transform: rotate(-90.0deg);*/
      /*!* Opera 10.5 *!*/
      /*-o-transform: rotate(-90.0deg);*/
      /*!* Saf3.1+, Chrome *!*/
      /*-webkit-transform: rotate(-90.0deg);*/
      /*!* IE6,IE7 *!*/
      /*filter: progid: DXImageTransform.Microsoft.BasicImage(rotation=0.083);*/
      /*!* IE8 *!*/
      /*-ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0.083)";*/
      /*!* Standard *!*/
      /*transform: rotate(-90.0deg);*/
    /*}*/
</style>