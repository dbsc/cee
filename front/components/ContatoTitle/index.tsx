import styles from './styles.module.scss'
export function ContatoTitle(){

    return (
        <div className={styles.container}>
            <div className={styles.content}>
                <div className={styles.title}>
                    <img src='/images/Ativo 2.svg' alt="Logo" />
                    <h1>Contato</h1>
                </div>
            </div>
        </div>
    )
}