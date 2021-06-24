import styles from './styles.module.scss'
export function QSTitle(){

    return (
        <div className={styles.container}>
            <div className={styles.content}>
                <div className={styles.title}>
                    <img src='/images/Time.jpg' alt="Time" />
                    <h1>Quem Somos</h1>
                    <p>
                        A <span>CEE</span> é uma liga universitária <br />
                        que trabalha para conectar os <br />
                        alunos do ITA às melhores <br />
                        oportunidades e <br />
                        empresas do mercado.
                    </p>
                </div>
            </div>
        </div>
    )
}