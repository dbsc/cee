import styles from './styles.module.scss'

export function Feira() {
	return (
        <div className={styles.container}>
            <div className={styles.content}>
                <h1>
                    Feira de Carreiras
                </h1>
                <img src="/images/Feira.png" alt="Feira" />
                <ul>
                    <li>Realizada anualmente em agosto.</li>
                    <li>O maior evento de recrutamento do ITA.</li>
                    <li>Atinge cerca de 75% de todos os alunos da graduação.</li>
                    <li>Evento ideal para maior contato direto os alunos do ITA.</li>
                    <li>Em stands, os alunos conversam diretamente com colaboradores de diversas áreas.</li>
                    <li>Oportuinidade para expor sua cultura, estilo de trabalho e conquistar os melhores talentos do ITA.</li>
                </ul>
            </div>
        </div>


    )
}