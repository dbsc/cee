import styles from './styles.module.scss'

export function Estagios() {
	return (
        <div className={styles.container}>
            <div className={styles.content}>
                <h1>
                    Estruturação de Estágios
                </h1>
                <p className={styles.Parag1}>
                    O ITA possui particularidades em relação à adequação de estágios ao calendário letivo. 
                    O 5º ano da graduação é composto por <span>um semestre voltado a estágios</span> e outro com garca horária reduzida, 
                    tornando o último ano um período <span>excelente para a adesão a estágios.</span>
                </p>
                <img src="/images/Estagio.png" alt="Estagio" />
                <p className={styles.Parag2}>
                    Contudo, muitos alunos conseguem conciliar um estágio com a graduação a partir, principalmente, do 3° ano. 
                    Assim, sua empresa tem a <span>disposição alunos do ITA em diversos momentos</span> de carreira para estagiar.
                    Muitos iteanos aderem aos <span>summer jobs</span> por conta dos quase 3 meses de férias no fim do ano, dedicando 1/3 disso 
                    inteiramente ao estágio.
                </p>
                <p className={styles.Parag2}>
                    Traçamos estratégias para empresas interessadas em recrutar iteanos conseguirem <span>ótimos candidatos e muitas 
                    inscrições</span> no seu processo. Prestamos <span>auxílio na parte burocrática</span>, temos contato direto com o ITA e fornecemos 
                    modelo de contratos de estágio.
                </p>
            </div>
        </div>


    )
}